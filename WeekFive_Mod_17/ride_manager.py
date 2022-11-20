class RideManager:
    def __init__(self) -> None:
        print("Ride manager activated")
        self.__availableCars = []
        self.__availableBikes = []
        self.__availableCngs = []

    def add_a_vehicle(self,vehicle_type,vehicle):
        if vehicle_type == 'car':
            self.__availableCars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__availableBikes.append(vehicle)
        else:
            self.__availableCngs.append(vehicle)

    def get_available_cars(self):
        return self.__availableCars
    
    def find_a_vehicle(self,rider,vehicle_type,destination):
        print("Looking for a car")
        if vehicle_type == 'car':
            if len(self.__availableCars)==0:
                print("Sorry No Car Available!")
                return False
            for car in self.__availableCars:
                # print('Potential',rider.location,car.driver.location)
                if abs(rider.location - car.driver.location) < 10:
                    distance = abs(rider.location - destination)
                    fare = distance * car.rate
                    if rider.balance < fare:
                        print('You do not have enough money for this trip',fare,rider.balance)
                        return False
                    if car.status == 'available':
                        car.status == 'unavailable'
                        self.__availableCars.remove(car)
                        rider.start_a_trip(fare)
                        print('Find a match for you for',fare)
                        return True



# Making a Ride Manager
uber = RideManager()