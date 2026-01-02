'''
Docstring for LAB3.lambda_filter
Filter & Lambda Functions 
Create programs that: 
1. Use filter() + a function to keep only even numbers 
2. Use filter() + lambda to keep only even numbers 
3. Filter names that have 3 or more characters 
4. Filter words that contain the letter "a"
'''
def even_num(num):
    return num % 2 == 0

lst1 = [1,2,3,4,5,6,7,8,9]

lst2 = list(filter(even_num,lst1))
print(lst2)

lst3 = list(filter(lambda x : x%2==0, lst1))
print(lst3)
name_lst = ['Ana','Sara','praba','john','Ani']
print("Original name list: ", name_lst)
long_names = list(filter(lambda y:len(y)>3, name_lst))
print("Names more than 3 letters",long_names)