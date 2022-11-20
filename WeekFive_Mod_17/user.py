import hashlib
from Brta import Brta
from vehicles import Car,Bike,Cng
from ride_manager import uber
import random

# Custom Exception
class UserAlreadyExist(Exception):
    def __init__(self,email, *args: object) -> None:
        super().__init__(*args)
        print(f'User {email} already exist!')


# Making Instance variable of Brta Class
licence_authority = Brta()


# Making User from Module 16-2
class User:
    def __init__(self,name,email,password) -> None:
        self.userName = name
        self.userEmail = email

        # Encrypting Password
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        
        # Checking If a user already exist
        already_exist = False
        with open('WeekFive_Mod_17/new.txt','r') as file:
            if email in file.read():
                # raise UserAlreadyExist(email)
                already_exist = True
        file.close()

        # Storing Password
        if already_exist==False:
            with open('WeekFive_Mod_17/new.txt','a') as file:
                file.write(f'{email} {pwd_encrypted}\n')
            file.close()

        # User Created Message
        # print(f'"{self.userName}" user created.')

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


# As a Rider, He/She also a User
# Making Rider Class that will be inherit User class
class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance

    # kon location a Rider ase ta kortipokkho jante pare ejonno set_location Method
    def set_location(self,location):
        self.location = location


    # To know Rider location
    def get_location(self):
        return self.location

    # A Rider can Request a trip in this method
    def request_trip(self,destination):
        pass

    # To Start a trip
    def start_a_trip(self,fare):
        self.balance -= fare



# Making a Driver Class That also inherit User class
class Driver(User):
    def __init__(self, name, email, password,location,licence) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.licence = licence
        self.valid_driver = licence_authority.validate_licence(email,licence)
        self.earning = 0

    # Take Driving Test to Driver
    def driving_test(self):
        result = licence_authority.take_driving_test(self.userEmail)
        if result==False:
            # print("Sorry you failed, Try Again!")
            self.licence = None
        else:
            self.licence = result
            self.valid_driver = True


    # For Register a vehicle
    def register_a_vehicle(self,vehicle_type,licence_plate,rate):
        if self.valid_driver is True:
            new_vehicle = None
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type,licence_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type,licence_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,new_vehicle)
            else:
                new_vehicle = Cng(vehicle_type,licence_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,new_vehicle)
        else:
            pass
            # print("You are not a valid driver")


    # Driver can start a trip
    def start_a_trip(self,destination,fare):
        self.earning += fare
        self.location = destination



# Making Riders
rider1 = Rider('rider1','rider1@gmail.com','rider1',random.randint(0,30),1000)
rider2 = Rider('rider2','rider2@gmail.com','rider2',random.randint(0,30),5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3',random.randint(0,30),5000)

# Making Drivers
for i in range(1,100):
    globals()[f'driver{i}'] = Driver(f'driver{i}',f'driver{i}@gmail.com',f'driver{i}',random.randint(0,100),5441631)
    globals()[f'driver{i}'].driving_test()
    globals()[f'driver{i}'].register_a_vehicle('car',1245,10)


print(uber.get_available_cars())
uber.find_a_vehicle(rider1,'car',random.randint(1,100))
uber.find_a_vehicle(rider1,'car',random.randint(1,100))
uber.find_a_vehicle(rider1,'car',random.randint(1,100))
uber.find_a_vehicle(rider1,'car',random.randint(1,100))
uber.find_a_vehicle(rider1,'car',random.randint(1,100))