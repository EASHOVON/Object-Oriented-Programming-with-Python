""" 

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.(don't use any python built in function)
Example :  pHitrOn.iO presents "Python COuRSe".
Ans : PhITRoN.Io PRENSENTS “pYTHON coUrsE”

"""

str = "pHitrOn.iO presents “Python COuRSe”"
str2 = ""
for i in range(len(str)):
    if str[i] == " ":
        str2 += " "
    elif str[i]==".":
        str2 += "."
    elif str[i] == "“":
        str2 += "“"
    elif str[i] == "”":
        str2 += "”"
    else:
        if ord(str[i])>=65 and ord(str[i])<=90:
            str2 += chr(ord(str[i])+32)
        elif ord(str[i])>=97 and ord(str[i])<=122:
            str2 += chr(ord(str[i])-32)
print(str2)