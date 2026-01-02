'''
Design an abstract base class that: 
o represents a role or capability 
o defines at least one abstract method 
2. Attempt to: 
o create a subclass that does not implement the method 
o instantiate it
'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_noise(self):
        print("Woof")

dog = Dog()
dog.make_noise()
dog.make_sound()