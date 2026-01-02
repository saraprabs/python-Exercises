'''
Functional list transformation 
Use a functional approach to transform a list of numbers. 
Apply one operation that changes the values and one operation that filters values. 
The solution must use lambda expressions together with built-in higher-order functions.
'''
def high_func(func, value):
    return func(value)

def square_func(num):
    return list(map(lambda x: x**2, num))

def even_func(lst1):
    return list(filter(lambda x: x%2==0, lst1))

num_lst = [2, 5, 7, 8, 10, 12]
print("Original list", num_lst)
print("Square number list ",high_func(square_func, num_lst))
print("Even number list ",high_func(even_func, num_lst))

