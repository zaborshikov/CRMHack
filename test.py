import sqlite3
conn = sqlite3.connect('moods.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS mood(
    moodsid TEXT,
    positive TEXT,
    negative TEXT);""")
conn.commit()