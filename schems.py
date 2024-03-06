class Book():
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
        self.author = []
        self.category = ''
        self.genre = []
        self.favorite = []
        self.buy = []
    
    def get_info_low(self):
        print(f'Название книги - {self.title}, цена {self.price}')

    def get_info_full(self):
        print(f'Название книги - {self.title}, цена {self.price}, категории {self.category}')
        
class Author():
    def __init__(self, id, fullname, date_born, date_death, biography):
        self.id = id
        self.fullname = fullname
        self.date_born = date_born
        self.date_death = date_death
        self.biography = biography
        self.books = []
    
    def get_info_low(self):
        print(f'ФИО - {self.fullname}, умер в {self.date_death}')
        
    def get_info_full(self):
        print(f'ФИО - {self.fullname}, родилься в {self.date_born}, умер в {self.date_death}')