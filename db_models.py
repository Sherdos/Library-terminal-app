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
        