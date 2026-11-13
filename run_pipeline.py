import subprocess
import time
import datetime
import os

def run_script(script_name):
    print(f"\n{'='*60}")
    print(f"🚀 RUNNING: {script_name}")
    print(f"{'='*60}\n")
    try:
        subprocess.run(["python", script_name], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Error running {script_name}. Moving to next step...")
        return False

def main():
    print(f"🤖 Starting Infinite Dosimetry Agent at {datetime.datetime.now()}")
    
    # Check if we have queries
    agent_success = run_script("agent_queries.py")
    
    if agent_success and os.path.exists("next_queries.txt"):
        run_script("search_papers.py")
        run_script("download_and_parse.py")
        run_script("summarize_papers.py")
    else:
        print("🛑 Agent failed to generate queries. Likely out of API requests.")

    print("\n🏁 Pipeline loop complete. Sleeping for 5 minutes before next loop...")
    time.sleep(300) # Sleep 5 mins

if __name__ == "__main__":
    while True:
        main()