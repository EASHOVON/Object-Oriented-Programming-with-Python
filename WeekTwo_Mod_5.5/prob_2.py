""" Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call. Receive the returned values and print the type. HInts: Please google how to return multiple values from a function in python """

def calculation(numOne,numTwo):
    add = numOne+numTwo
    if numOne<numTwo:
        temp = numOne
        numOne = numTwo
        numTwo = temp
    subtraction = numOne - numTwo
    return add, subtraction



jogfol,biogfol = calculation(40, 80)
print(f'Summation is {jogfol} \nand Subtraction is {biogfol} \nAlso type of this two number is : {type((jogfol,biogfol))}')
