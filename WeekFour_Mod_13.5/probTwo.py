""" 2. Call a function with and without a decorator. """

# Call Function with a decorator
""" def uppercase_decorator(func):
    def wrapper():
        make_uppercase = func().upper()
        return make_uppercase
    
    return wrapper


@uppercase_decorator
def say_hi():
    return "Hello There"

res = say_hi() #<-- calling function with a decorator
print(res) """

# Call Function without a decorator

def uppercase_decorator(func):
    def wrapper():
        make_uppercase = func().upper()
        return make_uppercase
    
    return wrapper

def say_hi():
    return "Hello There"

res = uppercase_decorator(say_hi)() # Calling a function without decorator
print(res)
