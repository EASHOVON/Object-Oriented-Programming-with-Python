""" 5-1 Introduction to list, list methods and slice.
The array is represented by List in Python. The list has some unique characteristics, unlike other programming languages. Slice is one of them. List also has some built-in methods to make our life easy. See the Reference """

# declaration of a list
numbers = [11, 13, 27, 15, 12, 49, 35]

# list is zero index based like other programming language
print(numbers[1]) # this will print 13

# Python list supports backward index, where index -1 refers the last element of the list, -2 refers the 2nd last element and so on ...
print(numbers[-2]) # this will print 49

# we can slice a list using colon (:), syntax is: list[start_index : end_index], where start_index is inclusive and end_index is exclusive
print(numbers[0:3]) # this will print [11, 13, 27]
print(numbers[:3]) # this will print all elements from index 0 to index 3 (exclusive)
print(numbers[3:]) # this will print all elements from index 3(inclusive) to end of the list


# we can also specify the sequence of slicing list. by default it is set to 1. see the examples below
print(numbers[0:6:1]) # this will print all elements from index 0(inclusive) to index 6(exclusive) one by one - [11, 13, 27, 15, 12, 49]
print(numbers[0:6:2]) # this will print all elements from index 0(inclusive) to index 6(exclusive), but it skip the index 1, 3, and 5. because we set the third parameter to 2

# slicing also works on negative index
print(numbers[5:2:-1]) # this will print the elements from index 5(inclusive) to index 2(exclusive) by going backward by one (-1)

print(numbers[::-1]) # this will print the entire array backward, also numbers[:] print the entire array

