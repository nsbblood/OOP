from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Runs on four legs"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def move(self):
        return "Flies in the sky"


dog = Dog()
print(f"Dog says: {dog.make_sound()}, {dog.move()}")

bird = Bird()
print(f"Bird says: {bird.make_sound()}, {bird.move()}")

#abstract base classes (ABCs)
