""" 5-6 One line for loop and condition using list comprehension
We can use for loop, condition, nested for loop (etc) in one line using python. It is called comprehension. Usage of excessive comprehension can complicate the code and reduce its readability. So avoid the usage of comprehension.
One example of comprehension is given below where the elements of result list will be odd number and divisible by 5 """
numbers = [11, 13, 27, 15, 12, 49, 35] # List

# result will be a list where elements are odd number and divisible by 5
result = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(result) # print -> [15, 35]

