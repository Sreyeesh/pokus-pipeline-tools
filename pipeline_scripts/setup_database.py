import sqlite3
import os

DB_PATH = "/studio/project/database/pipeline.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create assets table
cursor.execute("""
CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT,
    path TEXT,
    version TEXT,
    status TEXT
);
""")

# Create shots table
cursor.execute("""
CREATE TABLE IF NOT EXISTS shots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    description TEXT,
    folder TEXT,
    status TEXT
);
""")

# Create versions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id INTEGER,
    shot_id INTEGER,
    version TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(asset_id) REFERENCES assets(id),
    FOREIGN KEY(shot_id) REFERENCES shots(id)
);
""")

conn.commit()
conn.close()

print(f"✅ Database created at: {DB_PATH}")
