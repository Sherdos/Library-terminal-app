import psycopg2

from views import BookView, AuthorView




def main():
    conn = psycopg2.connect("dbname=library user=postgres password=2007")
    cur = conn.cursor()


    while True:
        print('1 - Книги, 2 - Авторы, 3 - Выйти')
        command = input('Введите комманду - ')
        if command == '1':
            while True:
                print('1 - посмотреть все книги, 2 поиск книги , 3 добавить книгу, 4 выйти')
                command = input('Введите комманду - ')
                book = BookView()
                if command == '1':
                    book.view_all_books(cur)
                elif command == '4':
                    print('Вернулись в Меню')
                    break
                elif command == '3':
                    book.view_add_book(cur)
                    conn.commit()
                elif command == '2':
                    book.view_search_book(cur)
        elif command == '2':
            while True:
                print('1 - посмотреть всех авторов, 2 поиск автора , 3 добавить автора, 4 выйти')
                command = input('Введите комманду - ')
                author = AuthorView()
                if command == '3':
                    author.add_author(cur)
                    conn.commit()
                elif command == '1':
                    author.view_all_authors(cur)
                elif command == '4':
                    print('Вернулись в Меню')
                    break
                    
        elif command == '3':
            print('Вы вышли из программы')
            break
                
        
        

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()