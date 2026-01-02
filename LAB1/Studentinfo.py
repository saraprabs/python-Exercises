'''
Docstring for Studentinfo
Ask user for: 
• Name 
• Age 
• Favorite subject 
• Favorite quote 
Then: 
1. Use formatting (.format() or f-strings) to print a nicely formatted paragraph. 
2. Capitalize the name. 
3. Remove whitespace around inputs. 
4. Create a list of the letters from the name. 
5. Print the first and last letter from that list. 
Goal: Combine strings, formatting, indexing, list creation.
'''
name = input("Student Name: ")
age = input("Age: ")
fav_subject = input("Favourite Subject: ")
fav_quote = input("Favourite Quote: ")
name=name.strip()
age=age.strip()
fav_subject = fav_subject.strip()
fav_quote = fav_quote.strip()

print(f"Student {name.upper()}, age {age}, favourite subject is '{fav_subject}', likes quote '{fav_quote}' ")

lst1 = [i for i in name]
print(lst1)
print(lst1[0],lst1[-1])