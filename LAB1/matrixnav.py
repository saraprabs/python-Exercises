'''
Docstring for matrixnav
Create three lists and nest them to form a matrix. Example: 
[ [1,2,3], 
[4,5,6], 
[7,8,9] ] 
Students must: 
1. Print the number in row 1, column 2 
2. Print the entire second row 
3. Print the diagonal (1,5,9) 
4. Create a new list of all first-column elements using indexing 
5. Then repeat using a list comprehension
'''
lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]
matrix = [lst_1 , lst_2 , lst_3]
print(matrix[0][1])
print(matrix[1])
diagonal = [matrix[i][i] for i in range(3)]
print(diagonal)
first_col=[]
for row in matrix:
    first_col.append(row[0])
print(first_col)
ny_lst= [matrix[i][0] for i in range(3)]
print(ny_lst)
