# We can pass a function as parameter of a function like-->

def do_something(work):
    print("Start the work")
    work()
    print("End of the work")


def do_work():
    print("My Work is done.")

# do_something(do_work)

# Also we can declare a function inside a function and we can call inside function and also return a function -->

def first_function():
    print("Inside First Function.")
    def second_function():
        print("Yea! I am a Second function")
    return second_function


# We can receive a returned function as a variable

#result = first_function()
#result() # We can call returned function like this

# Or We can call like -->
first_function()()