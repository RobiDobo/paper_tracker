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
    prompt = f"""You are an expert RF metrology engineer. 
I am building a frequency-selective personal RF/EMF dosimeter.

Here are the titles of the papers the AI marked as RELEVANT (Accepted):
{accepted_text}

Here are the titles of the papers the AI marked as IRRELEVANT (Rejected):
{rejected_text}

A standard frequency-selective dosimeter requires knowledge in these core pillars:
1. Sensors/Detectors (e.g., zero-bias Schottky diodes, thermocouples, thermopiles, FET-based detectors).
2. Antennas (e.g., broadband dipoles, Vivaldi, log-periodic, wearable/flexible).
3. Calibration/Metrology (e.g., E-field probes, anechoic chamber, standard gain horns, SAR phantoms).
4. Signal Processing/Hardware (e.g., log-detectors, SDRs, ADC filters).

TASK:
Analyze the accepted papers. Identify which of these core pillars or specific hardware components are UNDER-REPRESENTED in my research. 
Then, generate exactly 3 new arXiv search queries (using `abs:"keyword" OR abs:"keyword"`) to find the MISSING hardware components.
Ensure the queries are broad enough to find papers, but specific to hardware (avoid biology or network protocols).

Then, on the 4th line, generate exactly ONE search query for Europe PMC (focused on wearable medical sensors or health physics hardware).

CRITICAL RULES FOR ARXIV QUERIES:
1. Every single arXiv query MUST include at least one of these anchor terms: `abs:"wearable"`, `abs:"personal"`, `abs:"dosimeter"`, or `abs:"EMF"`. 
2. STRICTLY AVOID generating queries for: massive MIMO, satellite communications, UAVs, 5G base stations, quantum physics, or pure biology.
3. Example of a BAD query: abs:"antenna array". (Too broad)
4. Example of a GOOD query: abs:"wearable antenna" OR abs:"flexible antenna" AND abs:"EMF".

Output ONLY the 4 lines of queries. No numbering, no extra text.

CRITICAL: If you notice that the Accepted list hasn't changed since the last time you generated queries, you MUST pick a completely different pillar from the 4 listed above. For example, if the Accepted list is mostly Antennas, focus entirely on Calibration or Detectors. Do not repeat previous queries.

CRITICAL: Always use parentheses to group your OR/AND statements so they evaluate correctly. Example: (abs:"EMF" OR abs:"dosimeter") AND (abs:"wearable" OR abs:"personal")
"""
    
    pillar = random.choice(["Sensors/Detectors", "Antennas", "Calibration/Metrology", "Signal Processing/Hardware"])
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
