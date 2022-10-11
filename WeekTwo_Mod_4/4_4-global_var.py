""" 4-4 Access And Modify Global Variables
Normally, we can set value to a global variable from inside of a function. If we want to dose this, we have to need to use a special keyword global. But the best practice is to not change the value of a global variable from a local scope. See the example below - """

balance = 500

def total_cost(price, quantity):
    global balance # it is not recommended
    cost = price * quantity
    balance = cost
    return cost

cost = total_cost(5, 10)
print(cost)

print(f"balance = {balance}") # balance = 50

