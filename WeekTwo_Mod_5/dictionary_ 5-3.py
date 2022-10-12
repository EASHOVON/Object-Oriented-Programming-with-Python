""" 5-3 Explore Dictionary and Dictionary Methods
Dictionary is data structure where the elements are stored in key, value pairs. See the examples below - """

marks = {'Bangla': 85, 'English': 77, 'Math': 92}
print(marks) # print -> {'Bangla': 85, 'English': 77, 'Math': 92}

# Update an existing key's value
marks['English'] = 82

# Adding a new key and value
marks['Physics'] = 90

print(marks) # print -> {'Bangla': 85, 'English': 82, 'Math': 92, 'Physics': 90}

# Getting all 'keys'
keys = marks.keys()
print(keys) # print -> dict_keys(['Bangla', 'English', 'Math', 'Physics'])

# Getting all 'values'
values = marks.values()
print(values) # print -> dict_values([85, 82, 92, 90])

# Getting all key and value pairs
items = marks.items()
print(items) # print -> dict_items([('Bangla', 85), ('English', 82), ('Math', 92), ('Physics', 90)])

