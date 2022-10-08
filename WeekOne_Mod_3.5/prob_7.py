""" Write a program to check if the given number is a palindrome number.
Input : 121
Output : True
 """
inp_number = input("Number: ")

if inp_number == inp_number[::-1]:
    print("True")
else:
    print("False")