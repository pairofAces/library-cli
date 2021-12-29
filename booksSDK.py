from book import Book
import sqlite3
import os.path

l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

conn = sqlite3.connect(os.path.join(l, 'books.db'))

c = conn.cursor()

# create the table
c.execute('''CREATE TABLE IF NOT EXISTS books
              (title TEXT, pages INTEGER)''')

def cursor():

    l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return sqlite3.connect(os.path.join(l, 'books.db')).cursor()

# create a method to add a book
def add_book(book):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO books VALUES (?, ?)", (book.title, book.pages))
    c.connection.close()
    return c.lastrowid

# create a method to get a book by its title
def get_book_by_title(title):
    c = cursor()
    c.execute('SELECT * FROM books WHERE title=?', (title,))
    data = c.fetchone()

    if not data:
        return None
    
    return Book(data[0], data[1])

# create method to get all books
def get_books():
    c = cursor()
    books = []
    for row in c.execute('SELECT * FROM books'):
        books.append(Book(row[0], row[1]))
    c.connection.close()
    return books;

# create a method to update a book
def update_book(book, new_title, new_pages):
    c = cursor()
    with c.connection:
        c.execute('UPDATE books SET title=?, pages=? WHERE title=? AND pages=?',
        (new_title, new_pages, book.title, book.pages))
    book = get_book_by_title(book.title)
    c.connection.close()
    return book

# create method to delete a book
def delete_book(book):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM books WHERE title=? AND page=?', (book.title, book.pages))
    rows = c.rowcount
    c.connection.close()
    return rows
