import psycopg2
import conf 

from views import BookView, AuthorView




def main():
    try:
        conn = psycopg2.connect(f"dbname={conf.DBNAME} user={conf.USER} password={conf.PASSWORD}")
        cur = conn.cursor()


        while True:
            print('1 - Книги \n 2 - Авторы \n 3 - Выйти')
            command = input('Введите комманду - ')
            if command == '1':
                while True:
                    print('1 - посмотреть все книги \n 2 поиск книги \n 3 добавить книгу \n 4 выйти')
                    command = input('Введите комманду - ')
                    book = BookView(cur)
                    if command == '1':
                        book.view_all_books()
                    elif command == '2':
                        book.view_search_book()
                    elif command == '3':
                        book.view_add_book()
                        conn.commit()
                    elif command == '4':
                        print('Вернулись в Меню')
                        break
            elif command == '2':
                while True:
                    print('1 - посмотреть всех авторов \n 2 поиск автора \n 3 добавить автора \n 4 выйти')
                    command = input('Введите комманду - ')
                    author = AuthorView(cur)
                    if command == '1':
                        author.view_all_authors()
                    elif command == '2':
                        author.view_search_author()
                    elif command == '3':
                        author.add_author()
                        conn.commit()
                    elif command == '4':
                        print('Вернулись в Меню')
                        break
                        
            elif command == '3':
                print('Вы вышли из программы')
                break
    except:
        print('Ошибка')
    
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    main()