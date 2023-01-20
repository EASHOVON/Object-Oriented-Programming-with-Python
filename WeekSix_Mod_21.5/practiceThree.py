# Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class StrOperation:
    def __init__(self) -> None:
        self.string = self.get_string()

    def get_string(self):
        string = input("Enter a String to make it uppercase: ")
        return string

    def print_string(self):
        return self.string.upper()
    
res = StrOperation()

print(res.print_string())