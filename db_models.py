

from sqlite3 import Cursor


class BookDB():
    
    def __init__(self, cur):
        self.cur = cur
    
    def get_db_books(self) -> tuple|None: 
        self.cur.execute("select * from books;")
        books = self.cur.fetchall()
        return books
    
    def get_book(self, title):
        self.cur.execute('select * from books where title = %s', (title,))
        book = self.cur.fetchone()
        return book
    
    def add_book(self, title, price):
        try:
            self.cur.execute("insert into books(title, price) values (%s, %s)", (title, price))
            return True
        except:
            return False
    
    def get_category(self, id):
        self.cur.execute("select string_agg(c.title, ', ') from books as b join book_category as bc on bc.book_id = %s join categories as c on bc.category_id = c.id", (id,))
        category = self.cur.fetchone()
        return category
    
class AuthorDB():
    def __init__(self, cur:Cursor):
        self.cur = cur
    
    def add_author(self, data):
        try:
            self.cur.execute("insert into authors(fullname, date_born, date_death, biography) values (%s, %s, %s, %s)", data)
            return True
        except:
            return False
        
    def get_author(self, fullname):
        self.cur.execute('select * from authors where fullname = %s', (fullname,))
        author = self.cur.fetchone()

        return author
    
    def get_db_authors(self):
        self.cur.execute("select * from authors;")
        authors = self.cur.fetchall()
        return authors
