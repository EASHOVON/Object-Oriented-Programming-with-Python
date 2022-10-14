""" Create a python program that takes user input string and converts into
Capitalised 
Upper and
Lower case

Example Input: 
>> Enter your sentence: pHitRon

Output:
>> lower case: phitron
>> upper: PHITRON
>> capitalised: Phitron """

normalStr = input('Enter a string please: ')

inLowerCase = normalStr.lower()
inUpperCase = normalStr.upper()
inCapitalize = normalStr.capitalize()

print(f'lower case: {inLowerCase}')
print(f'upper case: {inUpperCase}')
print(f'capitalised: {inCapitalize}')