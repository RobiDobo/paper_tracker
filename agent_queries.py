import os
from openai import OpenAI
from db_manager import get_accepted_and_rejected
from dotenv import load_dotenv
import time
import random
from db_manager import init_db, get_accepted_and_rejected

load_dotenv()

client_gemini = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY"),
)


client_gemini_35 = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY"),
)
def generate_new_queries():
    # Ensure the database and status column exist before reading
    init_db() 
    
    # 1. Get what we accepted and what we rejected
    accepted_titles, rejected_titles = get_accepted_and_rejected()
    
    if not accepted_titles and not rejected_titles:
        print("Database has no YES/NO history yet. Generating blind queries based on the pillars...")

    accepted_text = "\n".join([f"- {t}" for t in accepted_titles]) if accepted_titles else "- None yet"
    rejected_text = "\n".join([f"- {t}" for t in rejected_titles]) if rejected_titles else "- None yet"
    
    print(f"Fetched {len(accepted_titles)} ACCEPTED and {len(rejected_titles)} REJECTED titles.")

    # 2. Ask the Metrology Expert AI to analyze the gaps
    prompt = f"""You are an expert RF metrology and hardware engineer. 
I am building a frequency-selective personal RF/EMF dosimeter.

Here are the titles of the papers the AI marked as RELEVANT (Accepted):
{accepted_text}

Here are the titles of the papers the AI marked as IRRELEVANT (Rejected):
{rejected_text}

A complete dosimeter requires knowledge in these core pillars:
1. Antennas & Sensor Arrays (e.g., broadband, flexible, array design, rectennas, Vivaldi).
2. Metrology & Calibration (e.g., E-field probes, SAR phantoms, anechoic chambers, calibration algorithms).
3. Signal Processing & Software (e.g., SDR, peak detection, RMS, log-detectors, embedded DSP, filtering).
4. Low-Power / Wearable Hardware (e.g., energy harvesting, flexible circuits, IoT sensors).

TASK:
Generate exactly 3 new arXiv search queries (using `abs:"keyword" OR abs:"keyword"`). 
CRITICAL: For this run, focus your queries HEAVILY on finding papers about: {pillar}.
Ensure the queries are specific to hardware/engineering (avoid pure biology or telecom network optimization).

Then, on the 4th line, generate exactly ONE search query for Europe PMC (focused on wearable medical sensors or health physics hardware).

Output ONLY the 4 lines of queries. No numbering, no extra text."""
    
    
    pillar = random.choice([
        "Antennas & Sensor Arrays", 
        "Metrology & Calibration", 
        "Signal Processing & Software", 
        "Low-Power Wearable Hardware"
    ])
    prompt = prompt + f"\nFor this run, focus your query generation HEAVILY on: {pillar}\n"
    
        # Try Gemini 3.1 first
    for attempt in range(2):
        try:
            response = client_gemini.chat.completions.create(
                model="gemini-3.1-flash-lite", messages=[{"role": "user", "content": prompt}], timeout=30
            )
            content = response.choices[0].message.content.strip()
            if "FIRST_NAME" in content or "LAST_NAME" in content or len(content) < 20:
                print("⚠️ AI generated a malformed query. Retrying...")
                continue # Skip this bad response and try again
            return content
        except Exception as e:
            if "429" in str(e) or "Rate limit" in str(e):
                print(f"    ⏳ Gemini 3.1 limit hit. Trying Gemini 3.5...")
                time.sleep(5)
                break # Break out to try 3.5
            else:
                print(f"Error: {e}")
                return None

    # Fallback to Gemini 3.5
    for attempt in range(3):
        try:
            response = client_gemini_35.chat.completions.create(
                model="gemini-3.5-flash-lite", messages=[{"role": "user", "content": prompt}], timeout=30
            )
            content = response.choices[0].message.content.strip()
            if "FIRST_NAME" in content or "LAST_NAME" in content or len(content) < 20:
                print("⚠️ AI generated a malformed query. Retrying...")
                continue # Skip this bad response and try again
            return content
        except Exception as e:
            if "429" in str(e) or "Rate limit" in str(e):
                print(f"    ⏳ Gemini 3.5 limit hit. Pausing 60 seconds... (Attempt {attempt+1}/3)")
                time.sleep(60)
            else:
                print(f"Error: {e}")
                return None
                
    print("Failed to generate queries after trying both Gemini models.")
    return None

if __name__ == "__main__":
    new_queries = generate_new_queries()
    if new_queries:
        print("\n--- AI Generated Queries ---")
        print(new_queries)
        
        # Save them so Phase 1 can read them later
        with open("next_queries.txt", "w") as f:
            f.write(new_queries)
        print("\n✅ Saved to next_queries.txt")
