""" 5-4 How to Loop through list, set, tuple and dictionary
We can loop through list, set, tuple, and dictionary using a simple for loop. See the examples below -
"""
numbers = [11, 13, 27, 15, 12, 49, 35] # List
numbers_set = {12, 22, 88, 66, 54, 99} # Set
numbers_tuple = 77, 89, 99, 44, 59, 90 # Tuple
marks = {'Bangla': 85, 'English': 82, 'Math': 92, 'Physics': 90} # Dictionary

# looping through 'list'
for num in numbers: # prints -> 11 13 27 15 12 49 35
    print(num, end=" ")
print("")

# Looping through 'set'
for num in numbers_set: # prints -> 66 99 54 22 88 12
    print(num, end=" ")
print("")

# Looping through 'tuple'
for num in numbers_tuple: # prints -> 77 89 99 44 59 90
    print(num, end=" ")
print("")

# Looping through 'dictionary'
for subject, mark in marks.items():
    print(subject, mark)
# prits (dictionary) ->
'''
Bangla 85
English 82
Math 92
Physics 90
'''

