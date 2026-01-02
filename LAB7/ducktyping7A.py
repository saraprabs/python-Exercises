'''
Duck typing
'''
def sdivide(a, b):
    try:
            result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers (int or float)."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    else:
        return f"Success! Result: {result}"
print(f"Integer division {sdivide(52, 8)}")
print(f"Float division { sdivide(25.5, 2)}")
print(f"invalid division {sdivide(25.5, '2')}")
print(f"edge {sdivide(25.5, None)}")