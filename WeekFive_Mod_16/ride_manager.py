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

    def match_a_vehicle(self):
        pass




# Making a Ride Manager
uber = RideManager()