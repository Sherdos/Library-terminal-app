import psycopg2

from views import BookView




def main():
    conn = psycopg2.connect("dbname=library user=postgres password=2007")
    cur = conn.cursor()


    while True:
        print('1 - посмотреть все книги, 2 выйти, 3 добавить книгу')
        command = input('Введите комманду - ')
        book = BookView()
        if command == '1':
            book.view_all_books(cur)
        elif command == '2':
            print('Вы вышли из программы')
            break
        elif command == '3':
            book.view_add_book(cur)
            conn.commit()
        
        

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()