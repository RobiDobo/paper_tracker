import subprocess
import time
import datetime

def run_script(script_name):
    print(f"\n{'='*60}")
    print(f"🚀 RUNNING: {script_name}")
    print(f"{'='*60}\n")
    try:
        # capture_output=False allows the logs to show up in GitHub Actions
        subprocess.run(["python", script_name], check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Error running {script_name}. Moving to next step...")
        return False

def main():
    start_time = time.time()
    MAX_RUN_TIME_SECONDS = 2 * 3600 # Run for 2 hours (7200 seconds)
    
    print(f"🤖 Starting Cloud Dosimetry Agent at {datetime.datetime.now()}")
    
    while True:
        # Check if we have been running for 2 hours
        if time.time() - start_time > MAX_RUN_TIME_SECONDS:
            print("\n⏰ 2 Hours reached. Stopping pipeline to save state and avoid GitHub timeout.")
            break
            
        print(f"\n🔄 Starting New Loop (Elapsed time: {int((time.time() - start_time)/60)} mins)")
        
        agent_success = run_script("agent_queries.py")
        if not agent_success:
            print("🛑 Agent failed (likely out of API keys). Sleeping for 5 minutes...")
            time.sleep(300)
            continue
            
        run_script("search_papers.py")
        run_script("download_and_parse.py")
        run_script("summarize_papers.py")
        
        print("\n🏁 Pipeline loop complete. Sleeping for 1 minute...")
        time.sleep(60)

if __name__ == "__main__":
    main()