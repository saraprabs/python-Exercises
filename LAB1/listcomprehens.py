'''
Docstring for listcomprehens
numbers = [1,2,3,4,5,6,7,8,9] 
Students must create using list comprehensions: 
1. A list of squares
2. A list of only even numbers 
3. A list of numbers doubled 
4. A list of only numbers greater than 5 
5. A list of strings: "Number: X" for each element
'''
numbers = [1,2,3,4,5,6,7,8,9]

square_lst = [i*i for i in numbers]
print("Square List", square_lst)

even_lst = [i for i in numbers if i % 2 == 0 ]
print("Even List", even_lst)

double_lst = [i*2 for i in numbers]
print("Double List", double_lst)

grt_lst = [i for i in numbers if i > 5 ]
print("Greater than 5 List", grt_lst)

x_lst = ['X' for i in numbers ]
print("X List", x_lst)