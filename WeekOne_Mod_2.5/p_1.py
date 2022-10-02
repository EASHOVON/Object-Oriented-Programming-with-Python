from math import ceil, floor


floatingNumber = float(input('Enter a Float Number: '))

floorNum = floor(floatingNumber)
ceilNum = ceil(floatingNumber)

print(f'For {floatingNumber} Floor is {floorNum} and Ceil is {ceilNum}')