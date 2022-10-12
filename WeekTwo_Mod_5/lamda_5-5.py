""" 5-5 Explore lamda with map, filter on list and dictionary
Usage of lamda function with map, filter on list and dictionary is given below - """

numbers = [11, 13, 27, 15, 12, 49, 35] # List

def squre(x):
    return x * x
print(squre(5))

# squre2 function do the same thing what squre() does above
squre2 = lambda x: x * x
print(squre2(9))

# Usage of 'lambda' using 'map' | 'map' iterate through the numbers 'list' and return the values by doubling them
doubled = map(lambda x: x * 2, numbers)
print(list(doubled)) # print the numbers list by doubling each of the elements -> [22, 26, 54, 30, 24, 98, 70]

# Usage of 'lambda' using 'filter' | 'filter' iterate through the numbers 'list' and return the values that are greater than 20
greater_than_20 = filter(lambda x: x > 20, numbers)
print(list(greater_than_20)) # print -> [27, 49, 35]

# A real world example of 'filter' and 'lambda'
players = [
    {'Name' : 'Shakib', 'Age' : 35},
    {'Name' : 'Tamim', 'Age' : 37},
    {'Name' : 'Mushfiq', 'Age' : 34},
    {'Name' : 'Mashrafi', 'Age' : 39},
    {'Name' : 'Miraz', 'Age' : 25},
]

senior_players = filter(lambda player: player['Age'] > 35, players)
print(list(senior_players)) # print -> [{'Name': 'Tamim', 'Age': 37}, {'Name': 'Mashrafi', 'Age': 39}]

junior_players = filter(lambda player: player['Age'] < 35, players)
print(list(junior_players)) # print -> [{'Name': 'Mushfiq', 'Age': 34}, {'Name': 'Miraz', 'Age': 25}]


""" Sometimes we have need to access the index with the value of a list. We can do it easily using enumerate() function. """
numbers = [11, 13, 27, 15, 12, 49, 35] # List
# usage of enumerate() function
for i, val in enumerate(numbers):
    print(i, val)
# printed ->
'''
0 11
1 13
2 27
3 15
4 12
5 49
6 35
'''

