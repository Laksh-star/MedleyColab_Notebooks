import sqlite3
import json
from datetime import datetime
import pandas as pd

def init_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            question TEXT NOT NULL,
            concepts TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_chat(timestamp, question, concepts):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO chat_history (timestamp, question, concepts, created_at)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, question, json.dumps(concepts), datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_chat_history():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('SELECT timestamp, question, concepts, created_at FROM chat_history ORDER BY id DESC')
    rows = c.fetchall()
    history = []
    for row in rows:
        history.append({
            'timestamp': row[0],
            'question': row[1],
            'concepts': json.loads(row[2]),
            'created_at': row[3]
        })
    conn.close()
    return history

def get_chat_history_df():
    history = get_chat_history()
    if not history:
        return None
    
    # Create DataFrame with all entries expanded
    df = pd.DataFrame(history)
    # Convert concepts list to comma-separated string
    df['concepts'] = df['concepts'].apply(lambda x: ', '.join(x))
    return df
