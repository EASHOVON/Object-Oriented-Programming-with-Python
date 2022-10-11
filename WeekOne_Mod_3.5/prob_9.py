""" Reverse a given integer number
Given:
76542

Expected output:
24567
 """

number = int(input("Enter a Number for Reverse: "))
rev = 0

while number>0:
    r = number%10
    rev = rev*10+r
    number//=10
print(rev,end="")