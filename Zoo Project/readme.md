ZOO SIMULATION SYSTEM – PYTHON OOP PROJECT

PROJECT DESCRIPTION

This project is an object-oriented zoo simulation implemented in Python. It models animals, their behaviours, and interactions with visitors over the course of a simulated day in a zoo.

The goal of the project is to demonstrate core Object-Oriented Programming concepts such as inheritance, encapsulation, method overriding, and polymorphism in a clear and practical way.

CLASS DESIGN

1. Animal (Base Class)

Animal class in the zoo with attributes

-   a_name : Name of animal
    

-   a_count : Number of animals
    

-   hunger leve l: to check amd feed the animal
    

-   energy_level : to maintain normal, high, low
    

-   fed_time : feeding time of the animal in a day
    

-   is_sleeping : attribute to track animal activity
    

Abstract methods:

-   make sound()
    

-   eat()
    

-   get_interaction_msg()
    

Class Methods:

-   adjust_hunger()  : helps to keep the hunger level in a range of 1 to 10
    

-   sleep() : increases energy level and sets sleeping status to true.
    

-   wakeup() : Display the current status of the animal
    

-   rest() : adjust the hunger and set energy level
    

-   roam(): reduces energy level and increases hunger of animal
    

2. Herbivores and Carnivores (Subclasses)

Inherits Animal super class

Implements the abstract methods

-   get_interaction_msg(): Message when a visitor interacts with animal.
    

-   eat(): Increase energy level and reduce hunger.
    

-   make_sound(): adjust energy level and hunger.
    

3. Visitor

Represents a visitor interacting with the animal

Attributes:

-   visitor name: v_name,
    

-   visitor id: v_id,
    

-   visiting time: v_time
    

Methods:

-   visit() : visitor visiting the animals in visiting time with a active list of animals and interacts with them based on the current status of animal. If its animals fed time then the visitor interacts and acts accordingly.
    

-   Interact(): visitor interaction with animal.
    

4. Zoo – Simulation Logic

Simulates a day in Zoo, animal activities, states and behaviour throughout the day along with visitor and animal interaction.

-   all_animals: list of all animals in zoo
    

-   visit_animal_list: active list of animals visited
    

Methods:

-   prepare_exhibits() : Filter the list of animals showcased today.
    

-   simulate_zoo_day() : Simulate a day at zoo from morning till night, animal behaviours, monitor states, visitors and interactions.
    

5. Execution Logic  : Animal Main python file:

-   load_data() : Loads data from Json file created for each species and instantiates the class and creates objects for all animals according to their species.
    

-   run_simulation(): Prepares active list of animals and runs simulation for set range of days.
    

SIMULATION FLOW

1. Morning

-   Animals wakes up, roams, make sound
    

2. Noon

-   Visitors visit
    

-   visitors Interact with animals
    

-   Display the status of animals
    

3. Afternoon

-   Animal rest, roam
    

4. Night

-   Sleeping time
    

-   Energy level increases further
    

-   adjust hunger
    

5. End of day status of animals.
