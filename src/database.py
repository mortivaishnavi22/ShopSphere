import sqlite3
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database and SQL schema locations
DB_PATH = BASE_DIR / "data" / "shopsphere.db"
SCHEMA_PATH = BASE_DIR / "sql" / "01_create_tables.sql"

def create_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        conn.executescript(schema)

        # Verify that the tables were created
        tables = conn.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            ORDER BY name
        """).fetchall()

        print("Database created successfully!")
        print(f"Location: {DB_PATH}")
        print("\nTables:")
        for table in tables:
            print(f"- {table[0]}")

if __name__ == "__main__":
    create_database()