import sqlite3
import json
import re

DB_NAME = "papers.db"

def spot_check_and_rescue():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Get all accepted papers
    cursor.execute("SELECT id, title FROM processed_papers WHERE status = 'YES'")
    accepted_papers = cursor.fetchall()
    
    print(f"Total ACCEPTED papers in DB: {len(accepted_papers)}\n")
    
    print("🔎 Spot check (10 random accepted papers):")
    print("-" * 60)
    for paper in accepted_papers[:10]: # Just show the first 10
        print(f"- {paper[1]}")
    print("-" * 60 + "\n")
    
    # Create the rescue JSON
    rescued_papers = []
    for paper in accepted_papers:
        paper_id = paper[0]
        title = paper[1]
        
        # We need to figure out if this is an arXiv ID or a DOI
        # to recreate the download link for Phase 2
        if re.match(r'^\d{4}\.\d{4,5}', paper_id): # Looks like an arXiv ID
            pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"
            status = 'ready_to_download'
        elif paper_id.startswith("PMC"):
            pdf_url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{paper_id}/fullTextXML"
            status = 'europe_pmc_fallback'
        else:
            # It's likely a DOI, we'll let Phase 2 try Unpaywall again
            pdf_url = None 
            status = 'ready_to_download'
            
        rescued_papers.append({
            "title": title,
            "doi": paper_id if not re.match(r'^\d{4}\.\d{4,5}', paper_id) else None,
            "arxiv_id": paper_id if re.match(r'^\d{4}\.\d{4,5}', paper_id) else None,
            "pmcid": paper_id if paper_id.startswith("PMC") else None,
            "pdf_url": pdf_url,
            "status": status
        })
        
    with open("papers_metadata.json", "w", encoding="utf-8") as f:
        json.dump(rescued_papers, f, indent=4, ensure_ascii=False)
        
    print(f"✅ Successfully exported {len(rescued_papers)} accepted papers to papers_metadata.json!")
    print("You can now run `python download_and_parse.py` and `python summarize_papers.py` to rescue these missing papers.")
    
    conn.close()

if __name__ == "__main__":
    spot_check_and_rescue()