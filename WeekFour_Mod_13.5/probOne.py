""" 1. Write a python program to find out the number of objects created for a certain class. """


class Employee:
    objCount = 0
    def __init__(self,name,age) -> None:
        self.empName = name
        self.empAge = age
        Employee.objCount += 1

    def get_emp_details(self):
        print(f'Emplyee Name: {self.empName}\nEmployee Age: {self.empAge}')



emp1 = Employee("Rakib",25)
emp2 = Employee("Sakib",30)
emp3 = Employee("Raju",29)

print(f'Number of object is: {Employee.objCount}')

