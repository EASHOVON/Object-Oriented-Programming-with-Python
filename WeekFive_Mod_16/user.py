import hashlib

# Making User from Module 16-2
class User:
    def __init__(self,name,email,password) -> None:
        self.userName = name
        self.userEmail = email

        # Encrypting Password
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        
        # Storing Password
        with open('WeekFive_Mod_16/new.txt','w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()

        # User Created Message
        print(f'"{self.userName}" user created.')

    # Static Method
    @staticmethod
    def log_in(email,password):
        stored_password = ""
        with open('WeekFive_Mod_16/new.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()

        hashed_pass = hashlib.md5(password.encode()).hexdigest()

        if stored_password==hashed_pass:
            print("Valid User")
            return True
        else:
            print("Invalid User")
            return False


# User
hero = User("Hero Alom","hero@alom.com","heroOhHero")

# When a user try to log in:
User.log_in("hero@alom.com","heroOhHero")