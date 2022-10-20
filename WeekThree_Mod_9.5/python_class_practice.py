class Vehicle:
    def __init__(self, name, mileage, capacity):
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