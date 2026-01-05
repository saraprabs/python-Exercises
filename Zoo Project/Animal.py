'''
Docstring for Zoo Project.Animals_Main
Zoo Simulation System 
This is the Main Animal parent class, Subclasses for different animal species Herbivores, Carnivores.
Defined methods for animal behaviors: make_sound, eat, get_interaction_msg, sleep, wake_up, rest, roam.
Uses abstract classes and methods that enforce polymorphism and abstraction.
'''
from abc import ABC, abstractmethod
from datetime import datetime
class Animal(ABC):
    def __init__(self, name, count, energy_level, fed_time):
        self.a_name = name
        self.a_count = count
        self.energy_level = energy_level  # energy level 1 -100
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
    
    def adjust_energy(self, amount):
        """Helper to keep energy between 0 and 100."""
        self.energy_level = max(0, min(100, self.energy_level + amount))

    def adjust_hunger(self, amount):
        """Helper to keep hunger between 0 and 10."""
        self.hunger_level = max(0, min(10, self.hunger_level + amount))

    def sleep(self):
        self.is_sleeping = True
        self.energy_level = 100
        return f"{self.a_name} is sleeping to recover energy."
    
    def wake_up(self):
        self.is_sleeping = False
        return f"{self.a_name} woke up!!"
    
    def rest(self):
        self.adjust_energy(10)
        self.adjust_hunger(2)
        return f"{self.a_name} is not moving, resting in shade... "
    
    def roam(self):
        self.adjust_energy(-20)
        self.adjust_hunger(5)
        return f"{self.a_name} is more active and lively... "
      
    def __str__(self):
        return f"[Animal] Name: {self.a_name:<10} | Count: {self.a_count:<10} | Energy_level: {self.energy_level:<10} | feeding time: {self.fed_time}"
    
        
class Herbivores(Animal):
    def __init__(self, name, count, energy_level, fed_time):
        super().__init__(name, count, energy_level, fed_time)
    
    def __str__(self):
        parent_str = super().__str__()
        return f"[Herbivore] {parent_str}"
    
    def get_interaction_msg(self):
        return f"tosses leaves and veggies to {self.a_name}"

    def eat(self):
        self.energy_level = 100
        self.hunger_level = 0 # Fully satisfied
        return f"{self.a_name} is fed..."
    
    def make_sound(self):
        self.adjust_energy(-5)
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
        self.energy_level = 100
        self.hunger_level = 0 # Fully satisfied
        return f"{self.a_name} is fed..."
    
    def make_sound(self):
        self.adjust_energy(-10)
        self.adjust_hunger(3)
        return f"{self.a_name} lets out a fierce roar..."

# --- Concrete Species ---
class Deer(Herbivores):
    def make_sound(self):
        self.adjust_energy(-5)
        return f"{self.a_name} (Deer) makes a soft grunting sound."
    
    def get_interaction_msg(self):
        return f"tosses some carrots to {self.a_name}."

    def dash(self): # Unique method
        self.adjust_energy(-20)
        return f"{self.a_name} spots a shadow and dashes quickly into the brush!"

class Lion(Carnivores):
    def make_sound(self):
        self.adjust_energy(-10)
        return f"{self.a_name} (Lion) lets out a mighty ROAR that shakes the ground!"

    def get_interaction_msg(self):
        return f"is awestruck by the majestic mane of {self.a_name}."

    def pride_call(self): # Unique method
        return f"{self.a_name} calls out to the rest of the pride."

class Elephant(Herbivores):
    def make_sound(self):
        self.adjust_energy(-15)
        return f"{self.a_name} (Elephant) trumpets loudly!"

    def get_interaction_msg(self):
        return f"watches {self.a_name} feeds sugarcanes & pineapples to elephant."

class Zebra(Herbivores):
    def make_sound(self):
        self.adjust_energy(-7)
        return f"{self.a_name} (Zebra) neighs energetically!"

    def get_interaction_msg(self):
        return f"feeds some fresh grass to {self.a_name}."

class Tiger(Carnivores):
    def make_sound(self):
        self.adjust_energy(-12)
        return f"{self.a_name} (Tiger) growls deeply!"

    def get_interaction_msg(self):
        return f"is fascinated by the stripes of {self.a_name}."
        
# class Birds(Animal):
#     def __init__(self, name, count, energy_level):
#         super().__init__(name, count, energy_level)
    
#     def __str__(self):
#         parent_str = super().__str__()
#         return f"[Birds] {parent_str}"

# class Aquatic_lives(Animal):
#     def __init__(self, name, count, energy_level):
#         super().__init__(name, count, energy_level)
    
#     def __str__(self):
#         parent_str = super().__str__()
#         return f"[Aquatic] {parent_str}"

# class Reptiles(Animal):
#     def __init__(self, name, count, energy_level):
#         super().__init__(name, count, energy_level)
    
#     def __str__(self):
#         parent_str = super().__str__()
#         return f"[Reptiles] {parent_str}"
    



