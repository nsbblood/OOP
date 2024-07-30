class Book:
    def __init__(self,title,author,pages,price):
        self.title=title
        self.author=author
        self.pages=pages
        self.price=price
        self.__secret="This is a secret attribute"

    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price-(self.price*self._discount)
        else:
            return self.price
    
    def setDiscount(self,amount):
        self._discount=amount
    


book1=Book("Brave New Malatya", "Leo Tolstoy", 1220 ,29.44)
book2=Book("War and Peace","Leo Tolstoy", 1220 ,29.44) 

print(book1._Book__secret) # This way you get secret message....

#let's say I did not ass the price or pages to book2 and printed book1... 
# then it would give errors again...

