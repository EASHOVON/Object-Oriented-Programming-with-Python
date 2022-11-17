from abc import ABC,abstractmethod

# Creating a Vehicle class
class Vehicle(ABC):
    speed = {
        'car' : 30,
        'bike' : 50,
        'cng' : 15
    }
    def __init__(self,vehicle_type,licence_plate,rate,driver) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.status = 'available'
        self.licence_plate = licence_plate
        self.speed = self.speed[vehicle_type]

    # Creating Abstract Method
    @abstractmethod
    def start_driving(self): 
        pass

    @abstractmethod
    def trip_finished(self):
        pass




# Now I am creating Car Class
class Car(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate, driver) -> None:
        super().__init__(vehicle_type, licence_plate, rate, driver)
        
    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.licence_plate,"Started")

    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type,self.licence_plate,"Completed Trip")

# Now I am creating Bike Class        
class Bike(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate, driver) -> None:
        super().__init__(vehicle_type, licence_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.licence_plate,"Started")

    def trip_finished(self):
        self.status = 'available'    
        print(self.vehicle_type,self.licence_plate,"Completed Trip")

# Now I am creating Cng class
class Cng(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate, driver) -> None:
        super().__init__(vehicle_type, licence_plate, rate, driver)

    def start_driving(self):
        self.status = 'unavailable'
        print(self.vehicle_type,self.licence_plate,"Started")

    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type,self.licence_plate,"Completed Trip")
