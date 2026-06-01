# create_db.py
import sqlite3
import os

DB_PATH = "research.db"

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            topic       TEXT NOT NULL,
            book_name   TEXT NOT NULL,
            file_path   TEXT NOT NULL,
            added_on    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
    print(f"Database created at: {DB_PATH}")


def add_book(topic: str, book_name: str, file_path: str):
    """Helper to insert a book entry."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (topic, book_name, file_path) VALUES (?, ?, ?)",
        (topic.lower().strip(), book_name, file_path)
    )
    conn.commit()
    conn.close()
    print(f"Added: [{topic}] {book_name}")


def list_books():
    """Print all entries in the DB."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, topic, book_name, file_path, added_on FROM books")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No books in database.")
        return

    for row in rows:
        print(f"[{row[0]}] Topic: {row[1]} | Book: {row[2]} | Path: {row[3]} | Added: {row[4]}")


if __name__ == "__main__":
    create_database()

    # --- Add your books here ---
    add_book(
        topic="distributed systems",
        book_name="Tanenbaum - Distributed Systems",
        file_path="books/tanenbaum_distributed_systems.pdf"
    )
    add_book(
        topic="operating systems",
        book_name="Tanenbaum - Modern Operating Systems",
        file_path="books/tanenbaum_modern_os.pdf"
    )
    add_book(
        topic="computer networks",
        book_name="Tanenbaum - Computer Networks",
        file_path="books/tanenbaum_computer_networks.pdf"
    )

    print("\n--- Books in DB ---")
    list_books()