'''
Animal Main to initialize the classes with data, Create a Visitor class and Zoo class to simulate a day at the zoo.
Visitor visits the active list of visiting animals. Simulates Visitor class interaction with animals. Activities of animlals in
a day at the zoo. Runs the simulation for multiple days.
'''
import json
from Animal import Deer, Lion, Elephant, Zebra, Tiger 
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
        if time_diff <= 120:
            print(f"Visitor {self.v_name } arrived during feeding window!")
            if animal.hunger_level >= 5:
                print(f"The {animal.a_name} looks hungry!")
                self.interact(animal)
                
            elif animal.is_sleeping:
                print(f"{animal.a_name} is asleep. {self.v_name} walks away quietly.")
            else:
                print(f"{animal.a_name} isn't interested in food right now (Hunger: {animal.hunger_level}/10).")
        else:
            print("Cannot feed animal now")
            print(f"{animal.a_name} is fed at {animal.fed_time} but visitor is here at {self.v_time}")
            return
        
    def interact(self, animal):
        # if isinstance(animal, Herbivores):
        #     print(f"{self.v_name} tosses leaves and veggies to {animal.a_name}")
        # else:
        #     print(f"{self.v_name} watches the animal from a safe distance {animal.a_name}")
        # Polymorphism in action, Python calls the correct version of interact based on the animals actual class
        message = animal.get_interaction_msg()
        print(f"{self.v_name} {message}")
        print(f"{animal.eat()}")
        return

class Zoo:
    def __init__(self, all_animals):
        self.day = 1
        self.all_animals = all_animals
        self.visit_animal_list =[]

    def prepare_exhibits(self, visiting_names):
        """Filters the master list for specific animals to show today."""
        self.visit_animal_list = [a for a in self.all_animals if a.a_name in visiting_names]

    def simulate_zoo_day(self, visiting_names, visitors):
        self.prepare_exhibits(visiting_names)
        hours_map = {
            "08:00 (Morning)": "08:00",
            "12:00 (Noon)": "12:00",
            "16:00 (Afternoon)": "16:00",
            "20:00 (Night)": "20:00"
            }
                    
        print(f"==================Day {self.day} at the ZOO===================")
           
        for label, time_str in hours_map.items():
            print(f"--- Current Zoo Time: {label} ---")
            current_sim_time = datetime.strptime(time_str, "%H:%M").time()

            current_visitors = [v for v in visitors if v.v_time == current_sim_time]
            if current_visitors:
                print(f"Visitors at the Zoo: {', '.join([v.v_name for v in current_visitors])}")

            for animal in self.visit_animal_list:
                # Noon & visitor interaction logic
                for visitor in current_visitors:
                    visitor.visit(animal)

                def feed_animal_check():
                    if animal.fed_time == current_sim_time and animal.hunger_level > 0:
                        print(f"[SCHEDULED FEEDING] It's {time_str}! {animal.eat()}")
                    return
                if "Morning" in label:
                    print(animal.wake_up())
                    print(animal.roam())
                    print(animal.make_sound())
                    feed_animal_check()
                elif "Afternoon" in label:
                    feed_animal_check() # Afternoon
                    if animal.energy_level < 50:
                        print(f"{animal.a_name} has low energy ({animal.energy_level}%).")
                        print(animal.rest())
                    else:
                        print(f"{animal.a_name} is still energetic ({animal.energy_level}%).")
                        print(animal.roam())
                elif "Night" in label:
                    print(animal.sleep())
                    animal.adjust_hunger(3)
        self.day+=1
        
#Load and combine data
def load_data():
    species_map = {
        "Deer": Deer,
        "Lion": Lion,
        "Elephant": Elephant,
        "Zebra": Zebra,
        "Tiger": Tiger
        # Add others as you create them
    }
    def load_json(path):
        with open(path, 'r') as f:
            raw_data = json.load(f)
            objects = []
            for data in raw_data:
                # Look up the class based on the name in JSON
                species_class = species_map.get(data['name'])
                if species_class:
                    objects.append(species_class(**data))
            return objects
            
    herb_list = load_json('c:/Users/Elev/python/Zoo Project/Herbivores.json')
    carn_list = load_json('c:/Users/Elev/python/Zoo Project/Carnivores.json')
    
    return herb_list + carn_list

#Multi-day simulation
def run_simulation(days):
    all_zoo_animals = load_data()
    my_zoo = Zoo(all_zoo_animals)
    active_list = ["Deer", "Zebra", "Elephant", "Lion", "Tiger"]

    #Simulate for visitors arriving at different times
    zoo_visitors = [
        Visitor("Alice", "V001", "12:00"),
        Visitor("Bob", "V002", "12:00"),   # Arrives at the same time as Alice
        Visitor("Charlie", "V003", "16:00"), # Arrives in the Afternoon
        Visitor("Diana", "V004", "08:00")    # Early bird visitor
    ]

    for _ in range(days):
        my_zoo.simulate_zoo_day(active_list, zoo_visitors)
        # Visual check of state persistence
        print(f"End of Day Status: {[(a.a_name, 'Energy:', a.energy_level) for a in my_zoo.visit_animal_list]}")
    print("-"*50)

if __name__ == "__main__":
    run_simulation(3)