class Publication:

    def __init__(self,price,page):
        self.price=price
        self.page=page


class Book(Publication):
    def __init__(self,price,page,author):
        super().__init__(price,page)
             #  self.price=price our class inherited it so we dont need it anymore
             # self.page=page
        self.author=author


class Mag:
    def __init__(self,price,period,publisher,page):

        self.price=price
        self.period=period
        self.publisher=publisher
        self.page=page

class Novel:
    def __init__(self,author,page,date,price):
        self.author=author
        self.page=page
        self.date=date
        self.price=price

n=Book(18.99,44,'Jack Ma')
print(n.author)
print(n.price)