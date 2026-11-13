import feedparser
import urllib.parse
import urllib.request

def fetch_latest_arxiv(query="dosimetry", max_results=5):
    base_url = "https://export.arxiv.org/api/query"
    # Build query parameters: search all fields, sort by submission date descending
    params = {
        "search_query": f"all:{query}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    # arXiv officially recommends controlling request frequency; add a simple retry or delay
    response = urllib.request.urlopen(url)
    feed = feedparser.parse(response.read())
    
    papers = []
    for entry in feed.entries:
        papers.append({
            "title": entry.title.strip(),
            "summary": entry.summary.strip(),  # This is the abstract, can be fed directly to the model
            "link": entry.link,
            "published": entry.published
        })
    return papers

# Test
papers = fetch_latest_arxiv("dosimetry", 3)
for p in papers:
    print(p["title"])
    print(p["link"])
    print("---")