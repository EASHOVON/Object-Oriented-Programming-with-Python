def remove_chars(str,n):
    sliced = str[n:]
    return sliced


testStr = input("Input a String: ")
num = int(input("Enter a Num: "))

print(remove_chars(testStr,num),end="")
