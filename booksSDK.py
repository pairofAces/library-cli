import sqlite3
import book from Book
import os.path

l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

conn = sqlite3.connect(os.path.join(l, 'books.db'))

c = conn.cursor()

