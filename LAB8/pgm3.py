'''
 Closure-based configuration 
Create a function that returns another function. 
The returned function should behave differently depending on a value captured from the 
outer function. Create at least two functions from the same factory function and demonstrate 
the difference in behavior. 
This pattern is known as a Function Factory. 
It leverages Closures, which allow an inner function to "remember" the environment 
(variables) of its outer function even after the outer function has finished executing.
'''
def power_factory(exponent):

    def calculate(base):
        return base ** exponent
    
    return calculate
# creating 2 functions from the factory
square_it = power_factory(2) #captures exponent 2
cube_it = power_factory(3)  #captures exponent 3

print(f"Square of 7: ,{square_it(7)}")
print(f"Cube of 7: ,{cube_it(7)}")
