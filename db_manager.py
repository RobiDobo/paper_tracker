import sqlite3

DB_NAME = "papers.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS processed_papers (
            id TEXT PRIMARY KEY,
            title TEXT,
            status TEXT,
            date_processed TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Try to add the 'status' column if it doesn't exist (for your existing DB)
    try:
        cursor.execute("ALTER TABLE processed_papers ADD COLUMN status TEXT")
    except sqlite3.OperationalError:
        pass # Column already exists
    conn.commit()
    conn.close()

def is_paper_processed(paper_id, title=None):
    if not paper_id and not title: return False
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Check by ID first
    if paper_id:
        cursor.execute("SELECT 1 FROM processed_papers WHERE id = ?", (paper_id,))
        if cursor.fetchone():
            conn.close()
            return True
            
    # Check by Title as a fallback
    if title:
        cursor.execute("SELECT 1 FROM processed_papers WHERE title = ?", (title,))
        if cursor.fetchone():
            conn.close()
            return True
            
    conn.close()
    return False
    
#added above ID check instead of only title

def mark_paper_processed(paper_id, title, status):
    if not paper_id: return
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT OR REPLACE INTO processed_papers (id, title, status) VALUES (?, ?, ?)", (paper_id, title, status))
        conn.commit()
    except sqlite3.IntegrityError:
        pass 
    conn.close()

def get_accepted_and_rejected():
    """Fetches the last 15 ACCEPTED and 15 REJECTED titles for the Agent."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT title FROM processed_papers WHERE status = 'YES' ORDER BY date_processed DESC LIMIT 15")
    accepted = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT title FROM processed_papers WHERE status = 'NO' ORDER BY date_processed DESC LIMIT 15")
    rejected = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    return accepted, rejected

def get_recent_titles(limit=30):
    """Kept for backwards compatibility."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM processed_papers ORDER BY date_processed DESC LIMIT ?", (limit,))
    titles = [row[0] for row in cursor.fetchall()]
    conn.close()
    return titles