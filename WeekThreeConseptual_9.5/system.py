class User:
    def __init__(self,name,roll,password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.returned_books = []


class Library:
    def __init__(self,book_list) -> None:
        self.book_list = book_list

allUsers = []
currentUser = None

while True:
    if currentUser == None:
        print("Not logged in\nPlease Login or create account (L/C)")
        option = input()
        if option =="L":
            roll = int(input("Roll: "))
            password = input("Password: ")
            match = False
            for user in allUsers:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    match = True
            if match == False:
                print("No user found")
        else:
            name = input("Name: ")
            roll = int(input("Roll: "))
            password = input("Password: ")
            user = User(name,roll,password)
            currentUser = user

    else:
        print("User er kaj ses")
        break