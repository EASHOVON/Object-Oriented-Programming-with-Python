class Vehicle:
    manufactures = "Japan"
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    # # This is normal getter and setter method 
    @property
    def get_vehicle_name(self):
        return self.name
    @property
    def set_vehicle_name(self,name):
        self.name = name

    # Getter and Setter Method with Decorator property
    @get_vehicle_name.getter
    def get_vehicle_name(self):
        return self.name
    @set_vehicle_name.setter
    def set_vehicle_name(self,name):
        self.name = name

    # __str__ methods
    def __str__(self):
        return 'Vehicles Name '+str(self.name)+' Milage '+str(self.mileage)

class Bus(Vehicle):
    pass

# School_bus = Bus("School Volvo", 12, 50)
# print(School_bus.getter_meth)

# Number One Task to check type of school_bus object
# print(type(School_bus))

# Number Two Task to check if the School_bus object is a instance of vehicle class
# print(isinstance(School_bus,Vehicle))

# Number Three Task --Define a property that must have the same value for every class instance (object)

premo_car = Vehicle("Premeo",20,60)
# print(School_bus.manufactures)
# print(premo_car.manufactures)

premo_car.set_vehicle_name = "Lambergeni"

vehicleName = premo_car.get_vehicle_name
# print(vehicleName)


print(premo_car)