import feedparser
import urllib.parse
import urllib.request
import os
from openai import OpenAI

# 1. Initialize OpenRouter client
# Be sure to set OPENROUTER_API_KEY in cmd first (refer to the previous set command)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

# 2. Fetch papers from arXiv
def fetch_latest_arxiv(query="dosimetry", max_results=3):
    base_url = "https://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    response = urllib.request.urlopen(url)
    feed = feedparser.parse(response.read())
    
    papers = []
    for entry in feed.entries:
        papers.append({
            "title": entry.title.strip(),
            "summary": entry.summary.strip(),
            "link": entry.link,
            "published": entry.published
        })
    return papers

# 3. Call the model to generate a summary
def summarize_paper(title, abstract):
    prompt = f"""You are a dosimetry research assistant. Please summarize this paper based on the title and abstract:
1. Core method (1 sentence)
2. Main conclusions (1 sentence)
3. Limitations or future work mentioned in the paper (1 sentence, if none are mentioned in the abstract, write "not mentioned in the abstract")

Title: {title}
Abstract: {abstract}"""
    
    # Use free models, remember to include the :free suffix
    response = client.chat.completions.create(
        model="openrouter/free", 
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

# 4. Main process
if __name__ == "__main__":
    print("Fetching the latest papers...\n")
    papers = fetch_latest_arxiv("dosimetry", 3)
    
    for i, p in enumerate(papers, 1):
        print(f"[{i}] {p['title']}")
        print(f"Link: {p['link']}")
        print("Generating AI summary...")
        summary = summarize_paper(p["title"], p["summary"])
        print(f"Summary:\n{summary}")
        print("-" * 50)
        
        # Add a short delay to prevent hitting the rate limit
        import time
        time.sleep(2)