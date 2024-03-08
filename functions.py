from schems import BaseSchem, Book

def get_all(items:tuple):
    data = []
    for i in items:
        item = input(f'Введите {i} - ')
        data.append(item)
    return tuple(data)
    

def view_all(items, schem:BaseSchem):
    for i in items:
        chem:BaseSchem = schem(*i)
        chem.get_info_low()     

def view_full(item:tuple, category:tuple):
    chem = Book(*item)
    chem.category = category[0]
    chem.get_info_full()                

