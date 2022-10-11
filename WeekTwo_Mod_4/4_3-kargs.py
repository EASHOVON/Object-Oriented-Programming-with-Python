""" 4-3 Explore Args And Kargs Together 1
Parameter defined by single star (*arg) treated as Tuple and defined by double star (**kargs) treated as Dictionary in Python. See the examples below - """

# 'num1' parameter will assign to the first argument and rest of the arguments will store in 'numbers' touple
def add(num1, *numbers):
    result = num1
    print(numbers) # it is a Tuple
    # Traversing Tuple
    for num in numbers:
        result += num
    return result
sum = add(5, 10, 20, 30)
print(sum)


def person(**kargs):
    print(kargs) # it is a Dictionary
    # Traversing Dictionary
    for key, value in kargs.items():
        print(key, value)

# each of the arguments will be a key:value pair of kargs dictionary in the function
person(name = "Shovon", age = "25", occupation = "Programmer")

