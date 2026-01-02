'''
Create: 
o one valid subclass 
o a second valid subclass with different behavior 
5. Write a function that: 
o accepts the abstract base class 
o calls the abstract method 
'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
    def most_liked_pets(animal:Animal):
        print("Cats are most liked pets!!!")
        animal.make_sound()
dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()
cat.most_liked_pets()