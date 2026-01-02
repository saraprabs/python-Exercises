'''
Docstring for LAB3.args_kwargs
*args and kwargs 
Create functions that: 
1. Accept any number of values using *args and return their sum 
2. Accept any number of values using *args and return the maximum 
3. Accept any number of keyword arguments using **kwargs and print them 
4. Combine a, *args, and **kwargs and print all arguments in a readable way
'''
def sum_args(*args):
    sum=0
    for i in args:
        sum += i
    return sum
print(sum_args(1,2,3,4,5))
print(sum_args(1,2,3,4,5,7,8,9,10))

def max_num(*args):
    return max(args)
print("Maximum number in a list",max_num(1,2,4,5,6,7,8,88,9,99))

def kw_args(**kwargs):
    print(kwargs)
kw_args(Name='Ana', Age = 32, Byear = 1988, Occupation= 'Engineer' )

def multi_args(a, *args, **kwargs):
    print(f"a = {a}")
    print("*args = {}".format(args))
    print("*kwargs = {}".format(kwargs))
multi_args('Hi','Hello','Ana','Welcome', Name='Ana', Age = 32, Byear = 1988)