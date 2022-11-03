import hashlib
class User:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt','w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()
        print(self.name, "user created")

    @staticmethod
    def log_in(email,password):
        stored_password = ''
        with open('users.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if stored_password == hashed_password:
            print("Valid User")
            return True
        else:
            print("Invalid User")
            return False


hero = User("Hero Alom","hero@alom.com","heroOhHero")
User.log_in('hero@alom.com','heroOhHero')