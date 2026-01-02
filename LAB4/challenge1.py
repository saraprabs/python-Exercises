'''
Docstring for LAB4.challenge1
 Tracking Variable Changes Across Scopes
Create a program that uses three nested functions. Each function should 
have a variable with the same name but different values. 
Use print statements to show exactly which value is used at each level, 
and experiment with both nonlocal and global to change the outcome
'''
fruit = 'banana'

def fn_A():
    global fruit
    print("Global fruit in FN A: ", fruit)
    fruit = 'apple'
    print("Changed global fruit inside FN A: ", fruit)
    def fn_B():
        fruit = 'orange'
        print("Local fruit inside FN B: ", fruit)
        def fn_C():
            nonlocal fruit
            print("Enclosed Fruit of FN B in C: ", fruit)
            fruit = 'mango'
            print("changed value of enclosed nonlocal fruit: ", fruit)

        fn_C()
    fn_B()        
fn_A()