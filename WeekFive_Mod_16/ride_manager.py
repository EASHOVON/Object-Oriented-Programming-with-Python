class RideManager:
    def __init__(self) -> None:
        print("Ride manager activated")
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cng = []

    def add_a_vehicle(self,vehicle_type,vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        elif vehicle_type == 'cng':
            self.__available_cng.append(vehicle)

    def get_available_cars(self):
        return self.__available_cars

    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type == 'car':
            if len(self.__available_cars) == 0:
                print("Sorry no cars is available")
                return False
            for car in self.__available_cars:
                # print('potential',rider.location,car.driver.location)
                if abs(rider.location - car.driver.location) < 10:
                    distance = abs(rider.location - destination)
                    fare = distance * car.rate
                    if rider.balance < fare:
                        print("You do not have enough money for this ride",fare,rider.balance)
                        return False
                    if car.status == 'available':
                        car.status = 'unavailable'
                        self.__available_cars.remove(car)
                        rider.start_a_trip(fare)
                        print("Find a match for you!",fare)
                        return True



uber = RideManager()