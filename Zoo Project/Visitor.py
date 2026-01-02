#visitor class
from Animal import Animal, Herbivores
from datetime import time

class Zoo:
    def __init__(self, animals):
        self.animals = animals

class Visitor:
    def __init__(self, name, id, v_time):
        self.v_name = name
        self.v_id = id
        self.v_time = v_time
    
    def visit(self, animal):
        print(f"{self.v_name} is visiting {animal}...")
        if self.v_time == animal.fed_time:
            print(f"Visitor {self.v_name } can now feed the animal")
    
visitor1 = Visitor("Alice", "1512", time(9,0))
visiting_animal = "Zebra"
animal = Animal()
for a in animal:
    if a.a_name == visiting_animal:
        visit_animal = a

       
visitor1.visit(visit_animal)

# Check the energy level after the visit
#print(f"Current energy of {found.a_name}: {first_animal.energy_level}")