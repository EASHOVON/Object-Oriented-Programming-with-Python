""" Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order
Hints: Search google about zip() function """

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i,j in zip(list1,list2[::-1]):
    print(i,j)