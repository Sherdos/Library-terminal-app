from schems import Book

def get_all(items):
    data = []
    for i in items:
        item = input(f'Введите {i} - ')
        data.append(item)
    return tuple(data)
    

def view_all(items, schem):
    for i in items:
        chem = schem(*i)
        chem.get_info_low()     

def view_all_full(items, schem):
    for i in items:
        chem = schem(*i)
        chem.cotegory = 
        chem.get_info_full()                

