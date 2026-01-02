'''
Docstring for Zoo Project.Animals_Main
Zoo Simulation System 
This is the Main Animal parent class
'''
from abc import ABC, abstractmethod
from datetime import datetime
class Animal(ABC):
    def __init__(self, name, count, energy_level, fed_time):
        self.a_name = name
        self.a_count = count
        self.energy_level = "normal"
        self.hunger_level = 5   # hunger level attribute to check & feed
        self.fed_time = datetime.strptime(fed_time, "%H:%M").time()
        self.is_sleeping = False
    
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def get_interaction_msg(self):
        pass 

    def adjust_hunger(self, amount):
        """Helper to keep hunger between 0 and 10."""
        self.hunger_level = max(0, min(10, self.hunger_level + amount))

    def sleep(self):
        self.is_sleeping = True
        self.energy_level = "high"
        return f"{self.a_name} is sleeping to recover energy."
    
    def wake_up(self):
        self.is_sleeping = False
        return f"{self.a_name} woke up!!"
    
    def rest(self):
        self.energy_level = "normal"
        self.adjust_hunger(2)
        return f"{self.a_name} is not moving, resting in shade... "
    
    def roam(self):
        self.energy_level = "low"
        self.adjust_hunger(5)
        return f"{self.a_name} is more active and lively... "
      
    def __str__(self):
        return f"[Animal] Name: {self.a_name:<10} | Count: {self.a_count:<10} | Energy_level: {self.energy_level:<10} | feeding time: {self.fed_time}"
    
    def __getitem__(self, index):
        return self.animals[index]
    
class Herbivores(Animal):
    def __init__(self, name, count, energy_level, fed_time):
        super().__init__(name, count, energy_level, fed_time)
    
    def __str__(self):
        parent_str = super().__str__()
        return f"[Herbivore] {parent_str}"
    
    def get_interaction_msg(self):
        return f"tosses leaves and veggies to {self.a_name}"

    def eat(self):
        self.energy_level = "high"
        self.hunger_level = 0 # Fully satisfied
        return f"{self.a_name} is munching on greens."
    
    def make_sound(self):
        self.energy_level = "normal"
        self.adjust_hunger(3)
        return f"{self.a_name} lets out a gentle bleat..."
    
                      
class Carnivores(Animal):
    def __init__(self, name, count, energy_level, fed_time):
        super().__init__(name, count, energy_level, fed_time)
    
    def __str__(self):
        parent_str = super().__str__()
        return f"[Carnivore] {parent_str}"
    
    def get_interaction_msg(self):
        return f"watches the animal from a safe distance {self.a_name}"

    def eat(self):
        self.energy_level = "high"
        self.hunger_level = 0 # Fully satisfied
        return f"{self.a_name} is feeding on meat."
    
    def make_sound(self):
        self.energy_level = "normal"
        self.adjust_hunger(3)
        return f"{self.a_name} lets out a fierce roar..."

class Birds(Animal):
    def __init__(self, name, count, energy_level):
        super().__init__(name, count, energy_level)
    
    def __str__(self):
        parent_str = super().__str__()
        return f"[Birds] {parent_str}"

class Aquatic_lives(Animal):
    def __init__(self, name, count, energy_level):
        super().__init__(name, count, energy_level)
    
    def __str__(self):
        parent_str = super().__str__()
        return f"[Aquatic] {parent_str}"

class Reptiles(Animal):
    def __init__(self, name, count, energy_level):
        super().__init__(name, count, energy_level)
    
    def __str__(self):
        parent_str = super().__str__()
        return f"[Reptiles] {parent_str}"
    



