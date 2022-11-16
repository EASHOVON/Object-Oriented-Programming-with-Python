import random

class Brta:
    def __init__(self) -> None:
        self.__licences = {}


    # For Take Driving test of a driver
    def take_driving_test(self,email):
        score = random.randint(0,100)
        if score >= 33:
            print("Congrats, You have passed the driving Test 😍",score)
            license_number = random.randint(414634131316541, 856556656565545)
            self.__licences[email] = license_number
            return license_number
        else:
            print("Sorry, You Have Failed 😪",score)
            return False

    # For Licence Validating
    def validate_licence(self,email,licence):
        for key,value in self.__licences.items():
            if key == email and value == licence:
                return True
        return False

    
