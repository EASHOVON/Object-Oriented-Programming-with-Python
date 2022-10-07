""" 
Display Fibonacci series up to 10 terms

0  1  1  2  3  5  8  13  21  34

"""

def printFibonacci(length):

    first = 0
    second = 1
    print(first,second,end=" ")
    length -= 2

    while length>0:
        print(first+second,end=" ")

        temp = second
        second = first+second
        first = temp
        length -=1

num = int(input("Enter a Num: "))
printFibonacci(num)
