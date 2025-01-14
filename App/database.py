import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS repositories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT,
            clone_path TEXT,
            created_at TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_repo(self, name, url, clone_path):
        query = "INSERT INTO repositories (name, url, clone_path, created_at) VALUES (?, ?, ?, datetime('now'))"
        self.conn.execute(query, (name, url, clone_path))
        self.conn.commit()

    def fetch_all(self):
        query = "SELECT * FROM repositories"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def delete_repo(self, repo_id):
        query = "DELETE FROM repositories WHERE id = ?"
        self.conn.execute(query, (repo_id,))
        self.conn.commit()
