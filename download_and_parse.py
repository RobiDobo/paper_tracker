import json
import os
import requests
import re
import time

os.makedirs("papers_pdf", exist_ok=True)
os.makedirs("papers_text", exist_ok=True)

def download_pdf(url, title):
    safe_title = re.sub(r'[^a-zA-Z0-9_\-]', '_', title)[:50]
    filepath = os.path.join("papers_pdf", f"{safe_title}.pdf")
    
    # If you manually placed the file here, skip!
    if os.path.exists(filepath):
        print(f"    ✅ File already exists locally: {filepath}")
        return filepath

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/pdf,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    
    try:
        print(f"    Downloading PDF from: {url}")
        response = requests.get(url, headers=headers, timeout=20, stream=True)
        if response.status_code == 200 and 'application/pdf' in response.headers.get('Content-Type', ''):
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"    ✅ PDF saved: {filepath}")
            return filepath
        else:
            print(f"    ❌ Failed (Status: {response.status_code}). Might be blocked.")
    except Exception as e:
        print(f"    ❌ Error downloading: {e}")
    return None

def fetch_europe_pmc_xml(pmcid, title):
    safe_title = re.sub(r'[^a-zA-Z0-9_\-]', '_', title)[:50]
    filepath = os.path.join("papers_text", f"{safe_title}_PMC.txt")
    
    if os.path.exists(filepath):
        print(f"    ✅ Text already exists: {filepath}")
        return filepath

    clean_pmcid = pmcid.replace("PMC", "")
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/PMC{clean_pmcid}/fullTextXML"
    
    try:
        print(f"    Fetching Full Text XML from Europe PMC for {pmcid}...")
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            raw_xml = response.text
            text = re.sub(r'<[^>]+>', ' ', raw_xml) 
            text = re.sub(r'\s+', ' ', text)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"    ✅ Full text saved: {filepath}")
            return filepath
        else:
            print(f"    ❌ Failed to fetch XML (Status: {response.status_code})")
    except Exception as e:
        print(f"    ❌ Error fetching XML: {e}")
    return None

def main():
    if not os.path.exists("papers_metadata.json"):
        print("papers_metadata.json not found. Run Phase 1 first.")
        return

    with open("papers_metadata.json", "r", encoding="utf-8") as f:
        papers = json.load(f)

    print(f"Loaded {len(papers)} papers from metadata. Starting Phase 2...\n")

    for i, p in enumerate(papers, 1):
        print(f"[{i}] {p['title'][:80]}...")
        
        # Strategy 1: Europe PMC XML
        if p.get('status') == 'europe_pmc_fallback' and p.get('pmcid'):
            fetch_europe_pmc_xml(p['pmcid'], p['title'])
            
        # Strategy 2: OA PDF
        elif p.get('status') == 'ready_to_download' and p.get('pdf_url'):
            download_pdf(p['pdf_url'], p['title'])
            
        # Strategy 3: Paywalled (Do nothing, wait for your manual drop)
        elif p.get('status') == 'not_found':
            # Check if you already dropped it in!
            safe_title = re.sub(r'[^a-zA-Z0-9_\-]', '_', p['title'])[:50]
            filepath = os.path.join("papers_pdf", f"{safe_title}.pdf")
            if os.path.exists(filepath):
                print(f"    ✅ Found manually dropped PDF: {filepath}")
            else:
                print("    ⏭️ Skipping (Waiting for your manual Sci-Hub download).")
            
        print("-" * 50)
        time.sleep(2)

if __name__ == "__main__":
    main()