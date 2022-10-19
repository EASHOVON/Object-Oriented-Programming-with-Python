import math
import time

def timer(func):
    def inner(*args,**kwargs):
        print("Time Start")
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print("Time End")
        print(start-end)
    return inner


@timer
def factorial(n):
    print(f'{n} factorial is: {math.factorial(n)}')

factorial(8)