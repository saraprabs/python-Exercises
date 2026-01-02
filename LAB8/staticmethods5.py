'''
 Static utility methods 
Create a class that acts as a utility container. 
The class should contain multiple static methods. 
Each static method should perform a small, independent operation. 
Demonstrate usage without creating any class instances.
'''
class Math:
    @staticmethod
    def sq_root(n):
        return n **0.5
    @staticmethod
    def cube_root(n):
        return n ** (1/3)
print(f"Square root of 7: {Math.sq_root(7):.2f}")
print(f"Cubee root of 7: {Math.cube_root(7):.2f}")