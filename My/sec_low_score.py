'''
Docstring for My.sec_low_score
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.
Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
    records=[]
    n=int(input())
    
    if n>=2 and n<=5:
        for _ in range(n):
            name = input()
            score = float(input())
            student += [name, score]
        
        grades = {j for i,j in student}
        
    else:
        print("invalid input")