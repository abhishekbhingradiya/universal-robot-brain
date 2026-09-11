from backend.database.db import get_connection


conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS global_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    strategy TEXT,
    avg_reward REAL
)
""")

conn.commit()
conn.close()

print("Database initialized")