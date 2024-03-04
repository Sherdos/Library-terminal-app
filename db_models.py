class BookDB():
    
    def get_db_books(self, cur):
        cur.execute("select * from books;")
        books = cur.fetchall()
        return books
    
    def get_book(self, cur, title):
        cur.execute('select * from books where title = %s', (title,))
        book = cur.fetchone()
        return book
    
    def add_book(self, cur, title, price):
        try:
            cur.execute("insert into books(title, price) values (%s, %s)", (title, price))
            return True
        except:
            return False
class AuthorDB():
    
    def add_author(self, cur, data):
        try:
            cur.execute("insert into authors(fullname, date_born, date_death, biography) values (%s, %s, %s, %s)", data)
            return True
        except:
            return False
        
    def get_author(self, cur, fullname):
        cur.execute('select * from authors where fullname = %s', (fullname,))
        author = cur.fetchone()
        return author
    
    def get_db_authors(self, cur):
        cur.execute("select * from authors;")
        authors = cur.fetchall()
        return authors
