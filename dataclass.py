from dataclasses import dataclass

@dataclass

class Book:
    author:str
    price:float
    page:int
    name:str
    year:int

b1=Book('Jack',19.99,500,'Latest book',1850)
b2=Book('Leo',14.99,250,'The Life',1888)
b3=Book('Jack',19.99,500,'Latest book',1850)
print(b1.page)
print(b1)

print(b1==b2)
print(b1==b3)

