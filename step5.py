class BigBoi:
    def __init__(self,color,price,):
        self.color=color
        self.price=price

class mBoi(BigBoi):
    def __init__(self,color,price,model,year):
        super().__init__(color,price) #The super() function should be used without the self argument
        self.model=model
        self.year=year

class Car(mBoi):
    def __init__(self,price,year,model,color,brand):
     #   self.price=price
        super().__init__(price,year,model,color)
      #  self.year=year
      #  self.model=model
    #    self.color=color
        self.brand=brand

class Motocycle(mBoi):
    def __init__(self,year,model,color,price):
       super().__init__(color,price,model,year)  #It is fixed - now it matches with mboi


       ''''' self.year=year
        self.model=model
        self.color=color
        self.price=price'''''

class Bike:
    def __init__(self,color,price):
        self.price=price
        self.color=color


newC=Car(25,1998,'C200','Blue','Mercedes')
print(newC.model)
newM=Motocycle(2011,'Bmw','red',20)
print(newM.price)

#The super() function should be used without the self argument

#Even if you change price,model and others in the parantheses it will inherit from mboi and
#give results accordingly... 