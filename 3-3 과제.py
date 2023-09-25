from abc import ABC, abstractmethod

class Item(ABC):
    count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.count += 1

    @abstractmethod
    def getprice(self):
        pass

class Book(Item):
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author

    def getprice(self):
        return f"Book Title: {self.title}, Price: ${self.price}, Author: {self.author}"

class Magazine(Item):
    def __init__(self, title, price, issue):
        super().__init__(title, price)
        self.issue = issue

    def getprice(self):
        return f"Magazine Title: {self.title}, Price: ${self.price}, Issue: {self.issue}"

if __name__ == '__main__':
    book1 = Book('소나기', 10000, 124, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난쏘공', 12000, 112, '조세희')
    magazine1 = Magazine('보그',11000, 9)
    magazine2 = Magazine('싱글즈',13000, 8)
    print('', book1,'\n', book2, '\n', book3, '\n', magazine1, '\n', magazine2)
    print('총',Item.count,'권')
    book2.getprice()
    magazine1.getprice()
    book1.getprice()
