from chems import Book


def get_author(cur, fullname):
    cur.execute('select * from authors where fullname = %s', (fullname,))
    author = cur.fetchone()
    return author


def add_author(cur, fullname ):
    date_born = input('Введите год рождение автора')
    date_death = input('Введите год смерти автора')
    biography = input('Введите биографию автора')
    cur.execute("insert into authors(fullname, date_born, date_death, biography) values (%s, %s, %s, %s)", (fullname, date_born, date_death, biography))
    author = get_author(cur=cur, fullname=fullname)
    return author

def get_all(items):
    data = []
    for i in items:
        item = input(f'Введите {i} - ')
        data.append(item)
    return data
    

def view_all(items):
    for i in items:
        chem = Book(id=i[0], title=i[1], price=i[2])
        chem.get_book_info_low()

