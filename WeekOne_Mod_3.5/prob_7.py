""" Write a program to check if the given number is a palindrome number.
Input : 121
Output : True
 """
# inp_number = input("Number: ")

# if inp_number == inp_number[::-1]:
#     print("True")
# else:
#     print("False")

n = int(input("Enter a Number: "))
temp = n
rev = 0

while n>0:
    r = n % 10
    rev = rev * 10 + r
    n //= 10

if temp==rev:
    print(True)
else:
    print(False)