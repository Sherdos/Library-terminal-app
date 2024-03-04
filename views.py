from schems import Book, Author
from db_models import BookDB, AuthorDB
from functions import get_all, view_all

class BookView:
    def __init__(self):
        self.book_db = BookDB()
        
        
    def view_all_books(self, cur):
        data = self.book_db.get_db_books(cur)
        view_all(data, Book)
        
    def view_add_book(self, cur):
        data = get_all(['Название книги', 'цену' ])
        result = self.book_db.add_book(cur, data[0], data[1])
        if result:
            print('Успешно')
        else:
            print('Ошибка')
    
    def view_search_book(self, cur):
        title = get_all(['Название книги'])
        result = self.book_db.get_book(cur, title[0])
        view_all((result, ))
        
class AuthorView:
    
    
    def __init__(self):
        self.author_db = AuthorDB()
   
    def view_all_authors(self, cur):
        data = self.author_db.get_db_authors(cur)
        view_all(data, Author)
    
    def add_author(self, cur):
        data = get_all(['ФИО', 'Дата рождение', "Дата смерти", "Биография" ])
        result = self.author_db.add_author(cur, data)
        if result:
            print('Успешно')
        else:
            print('Ошибка')
    