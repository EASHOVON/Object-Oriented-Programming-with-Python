""" 5-2 Introduction to set and tuple in python
Set is a data structure like List but set only contain unique values. A pair of curly braces are used to declare a set. We can add or remove any element from a set but it doesn’t maintain the sequence. See the examples below - """

# 'list' declaration
numbers = [12, 45, 15, 35, 89, 45, 15]
print(numbers)

# 'set' declaration
numbers_set = {12, 45, 15, 35, 89, 45, 15}
print(numbers_set) # print -> {35, 89, 12, 45, 15} because 'set' doesn't contain repeated value, it contains unique value only

# convert a 'list' to 'set'
set_from_list = set(numbers)

# add a value if the given value is not in the list
numbers_set.add(77)
print(numbers_set) # prints -> {35, 77, 89, 12, 45, 15}

# remove a value
numbers_set.remove(15)
print(numbers_set) # prints -> {35, 77, 89, 12, 45}


""" Tuple is also a immutable (adding a new element or deleting an existing one is not allowed) data structure like list. See the examples below - """
# 'list' declaration
numbers = [12, 45, 15, 35, 89, 45, 15]
print(numbers)

# 'tuple' declaration
numbers_tuple = 12, 45, 15, 35, 89, 45, 15

# another way to declare 'tuple'
another_tuple = (12, 45, 15, 35)

# convert a list to tuple
seted_from_list = tuple(numbers)
print(seted_from_list) # print -> (12, 45, 15, 35, 89, 45, 15)

