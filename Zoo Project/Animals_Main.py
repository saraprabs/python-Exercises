'''
Animal Main to initialize the classes with data, Create a Visitor class and Zoo class to simulate a day at the zoo.
Visitor visits the active list of visiting animals. Simulates Visitor class interaction with animals. Activities of animlals in
a day at the zoo. Runs the simulation for multiple days.
'''
import json
from Animal import Animal, Herbivores, Carnivores #, Birds, Reptiles, Aquatic_lives
from datetime import timedelta, datetime

class Visitor:
    def __init__(self, name, id, v_time):
        self.v_name = name
        self.v_id = id
        self.v_time = datetime.strptime(v_time, "%H:%M").time()
    
    def visit(self, animal):
        print(f"{self.v_name} is visiting {animal.a_name}...")
        # Define a 1-hour window (30 mins before or after)
        # We convert to 'datetime' briefly to use 'timedelta' for math
        dummy_date = datetime.today()
        now = datetime.combine(dummy_date, self.v_time)
        feed_time = datetime.combine(dummy_date, animal.fed_time)
        # Check if the difference is less than 60 minutes
        time_diff = abs((now - feed_time).total_seconds() / 60)
        if time_diff <= 60:
            print(f"Visitor {self.v_name } arrived during feeding window!")
            if animal.hunger_level > 7:
                print(f"The {animal.a_name} looks hungry!")
                self.interact(animal)
            elif animal.is_sleeping:
                print(f"{animal.a_name} is asleep. {self.v_name} walks away quietly.")
            else:
                print(f"{animal.a_name} isn't interested in food right now (Hunger: {animal.hunger_level}/10).")
        else:
            print("Cannot feed animal now")
            print(f"{animal.a_name} is fed at {animal.fed_time} but visitor is here at {self.v_time}")
    
    def interact(self, animal):
        # if isinstance(animal, Herbivores):
        #     print(f"{self.v_name} tosses leaves and veggies to {animal.a_name}")
        # else:
        #     print(f"{self.v_name} watches the animal from a safe distance {animal.a_name}")
        # Polymorphism in action, Python calls the correct version of interact based on the animals actual class
        message = animal.get_interaction_msg()
        print(f"{self.v_name} {message}")
        print(animal.eat())

class Zoo:
    def __init__(self, all_animals):
        self.day = 1
        self.all_animals = all_animals
        self.visit_animal_list =[]

    def prepare_exhibits(self, visiting_names):
        """Filters the master list for specific animals to show today."""
        self.visit_animal_list = [a for a in self.all_animals if a.a_name in visiting_names]

    def simulate_zoo_day(self, visiting_names):
        self.prepare_exhibits(visiting_names)
        hours = ["08:00 (Morning)", "12:00 (Noon)", "16:00 (Afternoon)", "20:00 (Night)"]
        visitor1 = Visitor("Alice", "1512", "12:00")
        # visiting_animals = ["Deer","Zebra","Elephant","Giraffe","Lion","Tiger","Bear","Wolf"]
        # self.visit_animal_list = [obj for obj in herbivores if obj.a_name in visiting_animals]
        # self.visit_animal_list += [obj1 for obj1 in carnivores if obj1.a_name in visiting_animals] 
    
        print(f"==================Day {self.day} at the ZOO===================")
        for time in hours:
            print(f"--- Time: {time} ---")
            for animal in self.visit_animal_list:
                if "Night" in time:
                    print(animal.sleep())
                    animal.adjust_hunger(3)
                elif "Morning" in time:
                    print(animal.wake_up())
                    print(animal.roam())
                    print(animal.make_sound())
                elif "Noon" in time:
                    visitor1.visit(animal)
                else: # Afternoon
                    if animal.energy_level in ["low", "normal"]:
                        print(animal.rest())
                    else:
                        print(animal.roam())
        self.day+=1
        
#Load and combine data
def load_data():
    def load_json(path, cls):
        with open(path, 'r') as f:
            return [cls(**data) for data in json.load(f)]
        
    herb_list = load_json('c:/Users/Elev/python/Zoo Project/Herbivores.json', Herbivores)
    carn_list = load_json('c:/Users/Elev/python/Zoo Project/Carnivores.json', Carnivores)
    
    return herb_list + carn_list

#Multi-day simulation
def run_simulation(days):
    all_zoo_animals = load_data()
    my_zoo = Zoo(all_zoo_animals)
    active_list = ["Deer", "Zebra", "Elephant", "Lion", "Tiger"]
    for _ in range(days):
        my_zoo.simulate_zoo_day(active_list)
        # Visual check of state persistence
        print(f"End of Day Status: {[(a.a_name, 'Energy:', a.energy_level) for a in my_zoo.visit_animal_list]}")

if __name__ == "__main__":
    run_simulation(3)