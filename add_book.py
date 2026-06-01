from create_db import add_book
import sys

if __name__ == "__main__":
    topic     = input("Topic (e.g. 'operating systems'): ").strip()
    book_name = input("Book name (e.g. 'Silberschatz - OS Concepts'): ").strip()
    file_path = input("PDF path (e.g. 'books/silberschatz_os.pdf'): ").strip()

    add_book(topic, book_name, file_path)