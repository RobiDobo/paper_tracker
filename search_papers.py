import requests
import json
import os
import time
import re
from datetime import datetime, timedelta
from openai import OpenAI
import feedparser
import sys
from dotenv import load_dotenv # <-- Add this
from db_manager import init_db, is_paper_processed, mark_paper_processed
import random

load_dotenv() # <-- Add this right here (before the clients)

# --- CONFIGURATION ---
YOUR_EMAIL = "robert.dobosan@student.upt.ro" 
# We use two different queries because arXiv and Europe PMC use different search syntax

# Read the AI-generated query if it exists, otherwise use the default
if os.path.exists("next_queries.txt"):
    with open("next_queries.txt", "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        
    if len(lines) >= 4:
        # Randomly pick one of the first 3 arXiv queries
        BASE_QUERY_ARXIV = random.choice(lines[:3])
        BASE_QUERY_PMC = lines[3]
        
        print(f"🧠 Using AI-generated arXiv query: {BASE_QUERY_ARXIV}")
        print(f"🧠 Using AI-generated PMC query: {BASE_QUERY_PMC}\n")
    else:
        print("⚠️ next_queries.txt is incomplete. Using defaults.\n")
        BASE_QUERY_ARXIV = 'abs:"wearable antenna"'
        BASE_QUERY_PMC = '("personal dosimeter")'
else:
    BASE_QUERY_ARXIV = 'abs:"RF dosimetry" OR abs:"wearable antenna"'
    BASE_QUERY_PMC = '("RF dosimetry" OR "personal dosimeter")'
    print(f"🤖 Using default queries.\n")

# NEW: How many NEW relevant papers do you want to process today?
TARGET_NEW_PAPERS = 30 
BATCH_SIZE = 10 # Fetch 10 at a time from the APIs
#INITIALIZE AI
# 1. Primary Client (OpenRouter)
client_openrouter = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

# 2. Fallback Client (Gemini)
client_gemini = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY"),
)
# model="gemini-2.5-flash"

# 3. Fallback Client 2 (Gemini 3.5)
client_gemini_35 = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY"),
)

# Change the flag to a tier counter
current_api_tier = 1 # 1=OpenRouter, 2=Gemini 3.1, 3=Gemini 3.5

import time
_last_request_time = 0

def enforce_rate_limit():
    global _last_request_time
    now = time.time()
    # Force a minimum of 5 seconds between EVERY request
    if now - _last_request_time < 5.0:
        sleep_time = 5.0 - (now - _last_request_time)
        time.sleep(sleep_time)
    _last_request_time = time.time()

use_gemini_only = False 

def check_relevance(title, abstract):
    global current_api_tier
    if not abstract: return "NO"
    
    prompt = f"""You are a strict research assistant evaluating papers for an RF engineering project.
My project is: "Designing a frequency-selective personal RF/EMF dosimeter (measuring 5G, Wi-Fi, etc.)".

Evaluate the title and abstract below. Is this paper USEFUL for building my project?

Say "YES" ONLY if the paper is about hardware that can be worn or held by a person. This includes:
- Wearable/flexible antennas
- Compact RF detectors (Schottky diodes, thermocouples) meant for portable use
- Calibration of personal exposure monitors
- Wearable RF harvesting hardware

Say "NO" for ANY of the following:
- Telecom infrastructure (Massive MIMO, base stations, satellite comms, UAV networks)
- Pure biology or health effects
- Ionizing radiation (X-rays)
- Quantum physics, photonics, or metamaterials not related to wearables

Answer ONLY with "YES" or "NO".
Title: {title}
Abstract: {abstract}"""
    
    # Waterfall logic: Try Tier 1, if it fails move to Tier 2, etc.
    while current_api_tier <= 3:
        enforce_rate_limit() # edit this to handle rate limiter
        try:
            if current_api_tier == 1:
                response = client_openrouter.chat.completions.create(
                    model="openrouter/free", messages=[{"role": "user", "content": prompt}], timeout=30)
            elif current_api_tier == 2:
                response = client_gemini.chat.completions.create(
                    model="gemini-3.1-flash-lite", messages=[{"role": "user", "content": prompt}], timeout=30)
            elif current_api_tier == 3:
                response = client_gemini_35.chat.completions.create(
                    model="gemini-3.5-flash-lite", messages=[{"role": "user", "content": prompt}], timeout=30)
            
            # If we get here, the API call succeeded!
            return "YES" if "YES" in response.choices[0].message.content.strip().upper() else "NO"
            
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "Rate limit" in error_msg:
                print(f"    ⚠️ Tier {current_api_tier} limit hit. Switching to Tier {current_api_tier + 1}...")
                current_api_tier += 1
                time.sleep(5) # Brief pause before trying the next model
            else:
                print(f"    ⚠️ AI Error on Tier {current_api_tier}: {error_msg}")
                return "ERROR"
                
    # If all 3 tiers fail
    print("    🛑 All API tiers exhausted for today.")
    return "ERROR"

def get_date_range(week_offset=0):
    """Calculates a 7-day window. week_offset=0 is today-7d to today, 1 is 14d to 7d, etc."""
    today = datetime.today()
    end_date = today - timedelta(days=(week_offset * 7))
    start_date = end_date - timedelta(days=7)
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
    
def search_europe_pmc(query, page_size, cursor_mark="*", week_offset=0):
    start_date, end_date = get_date_range(week_offset)
    full_query = f'({query}) AND FIRST_PDATE:[{start_date} TO {end_date}]'
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={full_query}&format=json&pageSize={page_size}&cursorMark={cursor_mark}"
    
    try:
        response = requests.get(url, timeout=15)
        data = response.json()
    except Exception as e:
        print(f"Error fetching PMC: {e}")
        return [], cursor_mark

    papers = []
    for result in data.get("resultList", {}).get("result", []):
        papers.append({
            "title": result.get("title"),
            "doi": result.get("doi"),
            "pmcid": result.get("pmcid"),
            "abstract": result.get("abstractText")
        })
    return papers, data.get("nextCursorMark", cursor_mark)

# arXiv doesn't strictly filter by date in the same way, so we sort by date and just pull the latest
def search_arxiv(query, page_size, start_index=0, week_offset=0):
    # We don't use week_offset in the URL, but we will just pull the next batch of papers
    print(f"Searching arXiv for: '{query}' (Start {start_index})...")
    url = f"http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results={page_size}&start={start_index}"
    
    try:
        response = requests.get(url, timeout=15)
        feed = feedparser.parse(response.content)
    except Exception as e:
        print(f"Error fetching arXiv: {e}")
        return []

    papers = []
    for entry in feed.entries:
        # This strips the 'v1', 'v2' from the ID
        raw_id = entry.id.split('/')[-1]
        clean_id = re.sub(r'v\d+$', '', raw_id) 
        
        papers.append({
            "title": entry.title.replace('\n', ' '),
            "abstract": entry.summary.replace('\n', ' '),
            "doi": entry.get('arxiv_doi', None),
            "pmcid": None,
            "arxiv_id": clean_id # <--- Using the clean ID
        })
        
    unique_papers = list({p['title']: p for p in papers}.values())
    return unique_papers
# -------------------------------------

def get_unpaywall_pdf(doi, email):
    if not doi: return None
    clean_doi = doi.replace("https://doi.org/", "").replace("doi:", "").strip()
    url = f"https://api.unpaywall.org/v2/{clean_doi}?email={email}"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("best_oa_location"):
                return data["best_oa_location"].get("url_for_pdf")
    except Exception: pass
    return None
    
def main():
    init_db()

    enriched_papers = []
    manual_drop = []
    
    new_relevant_count = 0
    max_deep_pages = 5 # Go 5 pages deep per query (50 papers)

    # Load all 3 arXiv queries and the 1 PMC query
    arxiv_queries = []
    pmc_query = ""
    if os.path.exists("next_queries.txt"):
        with open("next_queries.txt", "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        if len(lines) >= 4:
            arxiv_queries = lines[:3]
            pmc_query = lines[3]
    
    if not arxiv_queries:
        arxiv_queries = ['abs:"RF dosimetry" OR abs:"wearable antenna"']
        pmc_query = '("personal dosimeter")'

    print(f"Goal: Find {TARGET_NEW_PAPERS} NEW relevant papers. Let's go!\n")

    # 1. Fetch PMC first (just one page)
    print(f"--- Fetching PMC (Query: {pmc_query[:50]}...) ---")
    pmc_papers, _ = search_europe_pmc(pmc_query, BATCH_SIZE, "*", 0)
    batch_papers = pmc_papers

    # 2. Loop through ALL arXiv queries
    for query_idx, query in enumerate(arxiv_queries):
        if new_relevant_count >= TARGET_NEW_PAPERS:
            break

        print(f"\n=======================================================")
        print(f"🔎 Testing arXiv Query {query_idx + 1}/{len(arxiv_queries)}: {query[:60]}...")
        print(f"=======================================================")

        arxiv_start = 0
        for page_num in range(max_deep_pages):
            if new_relevant_count >= TARGET_NEW_PAPERS:
                break

            print(f"  --- Fetching Page {page_num + 1} (arXiv Start: {arxiv_start}) ---")
            
            arxiv_papers = search_arxiv(query, BATCH_SIZE, arxiv_start, 0)
            
            # If this query ran out of papers, break and move to the next query
            if not arxiv_papers:
                print(f"  ⏹️ No more papers for this query. Moving to next query.")
                break 

            # Add PMC papers only on the very first page of the first query
            if page_num == 0 and query_idx == 0:
                batch_papers = pmc_papers + arxiv_papers
            else:
                batch_papers = arxiv_papers
            
            for p in batch_papers:
                paper_id = p.get('doi') or p.get('arxiv_id')
                
                if is_paper_processed(paper_id, p['title']):
                    continue 
                    
                print(f"    [New] Checking: {p['title'][:60]}...")
                
                result = check_relevance(p['title'], p['abstract'])
                
                if result == "ERROR":
                    print("    ⏭️ Skipping due to AI error.")
                    time.sleep(5)
                    continue 
                    
                mark_paper_processed(paper_id, p['title'], result) 
                
                if result == "NO":
                    print("    ❌ AI marked as IRRELEVANT.")
                    time.sleep(4) 
                    continue
                    
                print("    ✅ AI marked as RELEVANT.")
                new_relevant_count += 1
                print(f"    🎯 Total relevant found: {new_relevant_count}/{TARGET_NEW_PAPERS}")
                
                # PDF LOGIC
                pdf_url = get_unpaywall_pdf(p['doi'], YOUR_EMAIL) if p.get('doi') else None
                if pdf_url:
                    p['pdf_url'] = pdf_url
                    p['status'] = 'ready_to_download'
                elif p.get('arxiv_id'):
                    p['pdf_url'] = f"https://arxiv.org/pdf/{p['arxiv_id']}.pdf"
                    p['status'] = 'ready_to_download'
                elif p.get('pmcid'):
                    p['pdf_url'] = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{p['pmcid']}/fullTextXML"
                    p['status'] = 'europe_pmc_fallback'
                else:
                    p['pdf_url'] = None
                    p['status'] = 'not_found'
                    manual_drop.append(p)
                    
                enriched_papers.append(p)
                time.sleep(4) 
                
                if new_relevant_count >= TARGET_NEW_PAPERS:
                    break
            
            arxiv_start += BATCH_SIZE
            time.sleep(4)

    # Save metadata
    with open("papers_metadata.json", "w", encoding="utf-8") as f:
        json.dump(enriched_papers, f, indent=4, ensure_ascii=False)
        
    print("\n" + "="*60)
    print(f"✅ Phase 1 complete. {len(enriched_papers)} NEW relevant papers saved to JSON.")
    
    if manual_drop:
        print("\n⚠️  ACTION REQUIRED (Paywalled):")
        for p in manual_drop:
            safe_title = re.sub(r'[^a-zA-Z0-9_\-]', '_', p['title'])[:50]
            print(f"- DOI: {p['doi']} -> Save as: {safe_title}.pdf")
    print("="*60 + "\n")
    
if __name__ == "__main__":
    main()