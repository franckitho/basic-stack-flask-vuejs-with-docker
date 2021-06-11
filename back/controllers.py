import sqlite3
DATABASE_NAME = "db/db.sqlite"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    return cursor.fetchall()