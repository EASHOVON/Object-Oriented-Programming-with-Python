import csv
from math import radians,sin,cos,atan2,sqrt
from Airport import Airport
class AllAirports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airport_data('WeekSix_Mod_21/data/airport.csv')

    def load_airport_data(self, file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}

        # get currency name <-----> rate
        with open("WeekSix_Mod_21/data/currencyrates.csv",'r') as file:
            lines = csv.reader(file)
            for line in lines:
                currency_rates[line[1]] = line[2]
        file.close() 

        # dictionary country <----> currency name
        with open("WeekSix_Mod_21/data/countrycurrency.csv","r") as file:
            lines = csv.reader(file)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()

        # Create Airport
        with open(file_path,'r',encoding="utf8") as file:
            lines = csv.reader(file)
            try:      
                for line in lines:
                    country = line[3]
                    if country not in country_currency:
                        continue
                    currency = country_currency[country]
                    if currency not in currency_rates:
                        continue
                    rate = currency_rates[currency]
                    airports[line[4]] = Airport(line[4],line[1],line[2],line[3],line[6],line[7],rate)
            except KeyError as e:
                print("Key Error",e)
            self.airports = airports
            # for airport in airports.items():
            #     print(airport)

    
    def get_distance_between_two_airports(self,lat1,lon1,lat2,lon2):
        radius = 6371
        lat_diff = radians(lat2 - lat1)
        lon_diff = radians(lon2 - lon1)
        a = (sin(lat_diff / 2) * sin(lat_diff / 2) +
         cos(radians(lat1)) * cos(radians(lat2)) *
         sin(lon_diff / 2) * sin(lon_diff / 2))
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = radius * c           
        return distance
    
    def distance_between_two_airports(self,airport1_code,airport2_code):
        airport1 = self.airports[airport1_code]
        airport2 = self.airports[airport2_code]
        distance = self.get_distance_between_two_airports(airport1.lat,airport1.lon,airport2.lat,airport2.lon)
        return distance
    
    def get_ticket_price(self,start,end):
        distance = self.distance_between_two_airports(start,end)
        airport1 = self.airports[start]
        fare = distance * airport1.rate
        return fare
    

# world_tour = AllAirports()
# fare = world_tour.get_ticket_price("DAC","PRA")
# print("Ticket Fare",fare)
