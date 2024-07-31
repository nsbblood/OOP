from dataclasses import dataclass

@dataclass

class Book:
    author:str
    price:float
    page:int
    name:str
    year:int

    def bookinfo(self):
        return f"{self.name} by {self.author}"


b1=Book('Ma',10,350,'Cool Light',1900)

b1.author='Anna'
b1.name='Sky is the limit'

print(b1.bookinfo())

