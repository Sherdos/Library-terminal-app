class Book():
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
        self.author = []
        self.category = []
        self.genre = []
        self.favorite = []
        self.buy = []
    
    def get_book_info_low(self):
        print(f'Название книги - {self.title}, цена {self.price}')
           