class Vehicle:
    manufactures = "Japan"
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    # This is normal getter and setter method 
    def getter(self):
        print("--------------Vehicle Info----------------")
        print(f'Vehicle Name: {self.name}, Vehicle Mileage: {self.mileage}, Vehicle Capacity: {self.capacity}')

    def setter(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)


# Number One Task to check type of school_bus object
print(type(School_bus))

# Number Two Task to check if the School_bus object is a instance of vehicle class
print(isinstance(School_bus,Vehicle))

# Number Three Task --Define a property that must have the same value for every class instance (object)

premo_car = Vehicle("Premeo",20,60)
print(School_bus.manufactures)
print(premo_car.manufactures)