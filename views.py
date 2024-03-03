from chems import Book
from db_models import BookDB
from functions import get_all, view_all

class BookView:
    def view_all_books(self, cur):
        book_db = BookDB()
        data = book_db.get_db_books(cur)
        view_all(data)
        
    def view_add_book(self, cur):
        data = get_all(['Название книги', 'цену' ])
        book= BookDB()
        result = book.add_book(cur, data[0], data[1])
        if result:
            print('Успешно')
        else:
            print('Ошибка')