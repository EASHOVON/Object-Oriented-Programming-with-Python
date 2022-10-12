# This is List Declaring called as numbers
numbers = [25,30,30,40,50,25,60,70,25]

numbers.append(85) # Here 85 will add at the last of the numbers list.

numbers.extend([100,200,300]) # Here 100,200,300 will add at the last of the numbers list.


numbers.insert(0,1000) # Insert an item at a given position.

numbers.remove(1000) # Remove the first item from the list whose value is equal to x.

numbers.pop() # Remove the item at the given position in the list, and return it.

print(numbers.index(30,0,4)) # This will check a value is in it or not in the specific position to position

print(numbers.count(25)) # Return the number of times x appears in the list.

numbers.sort(reverse=True) # This will be Sorting a List

print(numbers)


