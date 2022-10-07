""" Count all uppercase, lowercase, digits, and special symbols from a given

"P@#yn26at^&i5ve"
Total counts of chars, digits, and symbols 

Uppercase = 1
Lowercase = 7 
Digits = 3 
Symbol = 4
 """

from unicodedata import digit


str = input("Enter a String: ")

upCount = 0
lowCount = 0
digitCount = 0
symbolCount = 0

for ch in str:
    if(ord(ch)>=32 and ord(ch)<=47) or (ord(ch)>=58 and ord(ch)<=64) or (ord(ch)>=91 and ord(ch)<=96) or (ord(ch)>=123 and ord(ch)<=127):
        symbolCount += 1
    elif (ord(ch)>=48 and ord(ch)<=57):
        digitCount += 1
    elif (ord(ch)>=65 and ord(ch)<=90):
        upCount += 1
    elif (ord(ch)>=97 and ord(ch)<=122):
        lowCount += 1

print(f'Uppercase = {upCount}')
print(f'Lowercase = {lowCount}')
print(f'Digits = {digitCount}')
print(f'Symbol = {symbolCount}')