def res(numOne,numTwo):
    if numOne*numTwo <=1000:
        return numOne*numTwo
    else:
        return numOne+numTwo
numOne = int(input("Enter Num One: "))
numTwo = int(input("Enter Num Two: "))
result = res(numOne,numTwo)
print(f'The result is {result}')