'''
Practice EAFP-style error handling.
Write a function that: performs an operation on two inputs, may fail depending on the inputs
Implement it using: try , except 
3. Test the function with: valid inputs, invalid inputs, edge cases  
'''
def add(a,b):
    try:
        result = a + b
    except TypeError as e:
        return f"Error:Type mismatch. cannot add '{a}' type '{type(a).__name__}' and '{b}' type '{type(b).__name__}'"    
    except Exception as e:
        return f"Unexpected error {e}"
    else:
        return f"Success! {a} + {b} = {result}"
    # finally:
    #     print("Addition attempt complete")
print(add(10, 20))
print(add('Python',' Is Fun'))
print("Invalid ", add(50,'50'))
print(add([1,2],[3,4]))
print("Edge case ",add(None, 10))
