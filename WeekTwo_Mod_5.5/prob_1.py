""" Write a program to create a function show_employee() using the following conditions - 
- It should accept the employee’s name and salary and display both using a f string.
- If the salary is missing in the function call then assign default value 9000 to salary
- If the name is missing then assign a default value anonymous """

def show_employee(empName="anonymous", salary=9000):
    print(f'Name: {empName}, and Salary: {salary}')



show_employee("Shovon",25000)