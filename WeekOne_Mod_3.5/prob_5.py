"""
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
s1 = "Abc"
s2 = "Xyz"

"""

s1 = input("Enter a string One: ")
s2 = input("Enter a string Two: ")

s1_length = len(s1)
s2_length = len(s2)

length = s1_length if s1_length > s2_length else s2_length

s3 = ""

for i in range(length):
    s3 += s1[i]
    s3 += s2[s2_length-1]
    s2_length -= 1
print(s3)