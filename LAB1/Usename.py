'''
Doc Username Generator 
Ask the user for: 
• First name 
• Last name 
• Birth year 
Then generate a username using slicing, for example: 
f
irst 2 letters of first name + last 3 letters of last name + last 2 digits of birth yearstring for Usename
'''
first_name = input("Enter First Name: ")
last_name = input("Enter last Name: ")
birth_year = input("Enter birth year: ")

user_name = first_name[:2] + last_name[-3:] + birth_year[-2:]

print("User name :", user_name)
