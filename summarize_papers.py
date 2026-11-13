import os
import re
import time
import pymupdf
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# --- CLIENTS ---
client_openrouter = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ.get("OPENROUTER_API_KEY"))
client_gemini = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=os.environ.get("GEMINI_API_KEY"))
client_gemini_35 = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=os.environ.get("GEMINI_API_KEY"))

current_api_tier = 1
_last_request_time = 0

def enforce_rate_limit():
    global _last_request_time
    now = time.time()
    if now - _last_request_time < 5.0:
        sleep_time = 5.0 - (now - _last_request_time)
        time.sleep(sleep_time)
    _last_request_time = time.time()

def call_llm(prompt):
    global current_api_tier
    while current_api_tier <= 3:
        enforce_rate_limit() # rate limiter
        try:
            if current_api_tier == 1:
                res = client_openrouter.chat.completions.create(model="openrouter/free", messages=[{"role": "user", "content": prompt}], timeout=60)
            elif current_api_tier == 2:
                res = client_gemini.chat.completions.create(model="gemini-3.1-flash-lite", messages=[{"role": "user", "content": prompt}], timeout=60)
            elif current_api_tier == 3:
                res = client_gemini_35.chat.completions.create(model="gemini-3.5-flash-lite", messages=[{"role": "user", "content": prompt}], timeout=60)
            return res.choices[0].message.content
        except Exception as e:
            if "429" in str(e) or "Rate limit" in str(e):
                print(f"    ⚠️ Tier {current_api_tier} limit hit. Switching to Tier {current_api_tier + 1}...")
                current_api_tier += 1
                time.sleep(5)
            else:
                print(f"    ❌ Error on Tier {current_api_tier}: {e}")
                return ""
    return ""

# ... (Keep extract_text_from_pdf, clean_text, chunk_text the same) ...

def extract_text_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    text = ""
    for page in doc:
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (b[1], b[0])) 
        for b in blocks:
            text += b[4] + "\n"
    return text

def clean_text(text):
    text = re.sub(r'-\n', '', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def chunk_text(text, chunk_size=15000, overlap=500):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks

def summarize_chunk(chunk, title, chunk_num, total_chunks):
    prompt = f"""You are an expert in non-ionizing radiation dosimetry.
Read this section (Part {chunk_num} of {total_chunks}) of the paper titled "{title}".
Extract the key technical methods, data, and results related to dosimetry.
Keep it brief (2-3 sentences).

Text:
{chunk}"""
    return call_llm(prompt)

def generate_final_summary(title, chunk_summaries):
    combined = "\n".join(chunk_summaries)
    prompt = f"""Here are the extracted technical details from the paper titled "{title}":

{combined}

Based on these details, provide a final structured summary:
1. **Core Method**: What did they do?
2. **Main Conclusions**: What were the key dosimetry results?
3. **Limitations / Future Work**: What are the gaps mentioned by the authors?
"""
    return call_llm(prompt)
    

def process_file(filepath, filename):
    
    # --- NEW: Skip if already summarized ---
    out_file = os.path.join("summaries", f"summary_{filename}.md")
    if os.path.exists(out_file):
        return
    # ---------------------------------------    
    
    
    print(f"\nProcessing: {filename}")
    
    if filename.endswith('.pdf'):
        raw_text = extract_text_from_pdf(filepath)
    elif filename.endswith('.txt'):
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    else:
        return

    clean = clean_text(raw_text)
    if len(clean) < 1000:
        print("    ⚠️ Text too short, skipping.")
        return

    chunks = chunk_text(clean)
    print(f"    Split into {len(chunks)} chunks. Sending to LLM...")
    
    chunk_summaries = []
    for i, chunk in enumerate(chunks, 1):
        print(f"    -> Processing chunk {i}/{len(chunks)}...")
        summary = summarize_chunk(chunk, filename, i, len(chunks))
        if summary:
            chunk_summaries.append(summary)
        time.sleep(2) # Respect free API limits
    
    print("    Generating final structured summary...")
    final = generate_final_summary(filename, chunk_summaries)
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(f"# Summary for {filename}\n\n{final}")
    print(f"    ✅ Saved: {out_file}")

def main():
    os.makedirs("summaries", exist_ok=True)
    
    # Process PDFs
    if os.path.exists("papers_pdf"):
        for f in os.listdir("papers_pdf"):
            if f.endswith('.pdf'):
                process_file(os.path.join("papers_pdf", f), f)
                
    # Process TXTs
    if os.path.exists("papers_text"):
        for f in os.listdir("papers_text"):
            if f.endswith('.txt'):
                process_file(os.path.join("papers_text", f), f)

if __name__ == "__main__":
    main()