import sqlite3

def init_db():
    conn = sqlite3.connect("receipts.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY,
            vendor TEXT,
            date TEXT,
            amount REAL,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(vendor, date, amount, category):
    conn = sqlite3.connect("receipts.db")
    c = conn.cursor()
    c.execute("INSERT INTO receipts (vendor, date, amount, category) VALUES (?, ?, ?, ?)",
              (vendor, date, amount, category))
    conn.commit()
    conn.close()

def fetch_all_data():
    conn = sqlite3.connect("receipts.db")
    c = conn.cursor()
    c.execute("SELECT * FROM receipts")
    data = c.fetchall()
    conn.close()
    return data
