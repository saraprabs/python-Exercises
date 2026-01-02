"""
String Methods Investigation 
Using a string from user input, students must show: 
1. Uppercase version 
2. Lowercase version 
3. How many characters the string has 
4. Split the string into words 
5. Replace one letter with another
"""
user_string = input("Enter string : ")

print("Uppercase : ",user_string.upper())
print("Lowercase: ",user_string.lower())
print("String Length: ",len(user_string))
print("Splitted string  ",user_string.split())
print("Replace letter 'a' with 'o' ", user_string.replace('a','o'))