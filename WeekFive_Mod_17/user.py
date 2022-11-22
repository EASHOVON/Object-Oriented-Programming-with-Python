import hashlib
from Brta import Brta
from vehicles import Car,Bike,Cng
from ride_manager import uber
import random
import threading

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
        self.__trip_history = []

    # kon location a Rider ase ta kortipokkho jante pare ejonno set_location Method
    def set_location(self,location):
        self.location = location


    # To know Rider location
    def get_location(self):
        return self.location

    # A Rider can Request a trip in this method
    def request_trip(self,destination):
        pass

    # Get Trip History
    def get_trip_history(self):
        return self.__trip_history

    # To Start a trip
    def start_a_trip(self,fare,trip_info):
        print(f'A trip started for {self.userName}')
        self.balance -= fare
        self.__trip_history.append(trip_info)


# Making a Driver Class That also inherit User class
class Driver(User):
    def __init__(self, name, email, password,location,licence) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.licence = licence
        self.valid_driver = licence_authority.validate_licence(email,licence)
        self.earning = 0
        self.vehicle = None

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
                self.vehicle = Car(vehicle_type,licence_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_type,licence_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            else:
                self.vehicle = Cng(vehicle_type,licence_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
        else:
            pass
            # print("You are not a valid driver")


    # Driver can start a trip
    def start_a_trip(self,start,destination,fare,trip_info):
        self.earning += fare
        self.location = destination
        # Start a Thread
        trip_thread = threading.Thread(target=self.vehicle.start_driving,args=(start,destination))
        trip_thread.start()
        # self.vehicle.start_driving(start,destination)
        self.__trip_history.append(trip_info)



# Making Riders
rider1 = Rider('rider1','rider1@gmail.com','rider1',random.randint(0,30),1000)
rider2 = Rider('rider2','rider2@gmail.com','rider2',random.randint(0,30),5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3',random.randint(0,30),5000)
rider4 = Rider('rider4','rider4@gmail.com','rider4',random.randint(0,30),5000)
rider5 = Rider('rider5','rider5@gmail.com','rider5',random.randint(0,30),5000)

# Making Drivers
for i in range(1,100):
    globals()[f'driver{i}'] = Driver(f'driver{i}',f'driver{i}@gmail.com',f'driver{i}',random.randint(0,100),5441631)
    globals()[f'driver{i}'].driving_test()
    globals()[f'driver{i}'].register_a_vehicle('bike',1245,10)


print(uber.get_available_cars())
uber.find_a_vehicle(rider1,'bike',random.randint(1,100))
# uber.find_a_vehicle(rider2,'car',random.randint(1,100))
# uber.find_a_vehicle(rider3,'car',random.randint(1,100))
# uber.find_a_vehicle(rider4,'car',random.randint(1,100))
# uber.find_a_vehicle(rider5,'car',random.randint(1,100))

print(rider1.get_trip_history())
print(uber.total_income())