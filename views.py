from schems import Book, Author
from db_models import BookDB, AuthorDB
from functions import get_all, view_all

class BookView:
    def __init__(self, cur):
        self.book_db = BookDB(cur)
        
        
    def view_all_books(self):
        data = self.book_db.get_db_books()
        view_all(data, Book)
        
    def view_add_book(self):
        data = get_all(['Название книги', 'цену' ])
        result = self.book_db.add_book(data[0], data[1])
        if result:
            print('Успешно')
        else:
            print('Ошибка')
    
    def view_search_book(self ):
        title = get_all(['Название книги'])[0]
        result = self.book_db.get_book( title)
        view_all((result, ),Book)
        
class AuthorView:
    
    
    def __init__(self, cur):
        self.author_db = AuthorDB(cur)
   
    def view_all_authors(self):
        data = self.author_db.get_db_authors()
        view_all(data, Author)
    
    def add_author(self, ):
        data = get_all(['ФИО', 'Дата рождение', "Дата смерти", "Биография" ])
        result = self.author_db.add_author( data)
        if result:
            print('Успешно')
        else:
            print('Ошибка')
            
    def view_search_author(self, ):
        fullname = get_all(['ФИО автора'])[0]
        result = self.author_db.get_author( fullname)
        if result is None:
            print('Нет такого автора')
            return
        view_all((result, ), Author )
    