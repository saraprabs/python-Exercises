'''
Docstring for LAB5.nestedcomp15
Create a nested comprehension. Generate a two-dimensional structure (like a 
table or grid) with nested comprehensions. SECTION 4 — Combined OOP + 
Scope + Pythonic Techniques 
'''
SIZE = 6

multiplication_matrix = [[i * j for j in range(SIZE)] for i in range(SIZE) ]


print(f"{SIZE}x{SIZE} Multiplication Matrix:")

for row in multiplication_matrix:
    # Right-justify each number for table alignment
    print(" | ".join(f"{num:4d}" for num in row))

