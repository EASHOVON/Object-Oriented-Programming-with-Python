# import math
# import time

# def timer(func):
#     def inner(*args,**kwargs):
#         print("Time Start")
#         start = time.time()
#         func(*args,**kwargs)
#         end = time.time()
#         print("Time End")
#         print(start-end)
#     return inner


# @timer
# def factorial(n):
#     print(f'{n} factorial is: {math.factorial(n)}')

# factorial(8)

""" Assigning Functions to Variables """
def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)


""" Defining Functions Inside other Functions """
def plus_one(number):
    def add_one(number):
        return number + 1
    result = add_one(number)
    return result
plus_one(4)


""" Passing Functions as Arguments to other Functions """
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)


""" Functions Returning other Functions """
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()

