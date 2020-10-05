from datetime import timedelta 
class Itinerary():

    def __init__(self,origin_code):
        """
        :param origin_code: String, code of the inital airport  
        """
        self.string_path = [origin_code]
        self.path = []
        self.price = 0
        self.bag_price = 0
        self.max_bags = 0
        self.waiting_time = timedelta(hours= 0)

    def add(self, flight):
        """
        Appends a flight to our path and sums the cost of taking that flight
        """
        if len(self.path)>=1:
            self.waiting_time += flight.departure - self.path[-1].arrival 

        if flight.bags_allowed > self.max_bags:
            self.max_bags = flight.bags_allowed

        self.price += flight.price
        self.bag_price += flight.bag_price
        
        self.string_path.append(flight.destination)
        self.path.append(flight)
        

        
    def is_on_time_for(self,departure_time,min_transfer, max_transfer):
        """
        Checks if we can get on time for a departure time given
        a minimum and maximum time we have to wait

        :param datetime departure_time: time to check
        :param int min_transfer: minimun time we wait in hours
        :param  int max_transfer: maximum time we wait in hours
        :return Boolean: true if we can take a flight at the given time
        """
        last_arival = self.get_last_arival()
        if last_arival is None:
            #if it has no last_rival it means that this is the fitst departure time
            return True
        else:
            dif = departure_time - last_arival
            return dif >= timedelta(hours=min_transfer) and dif <= timedelta(hours=max_transfer)

    def get_origin(self):
        """
        :return str: code of the first departure airport
        """
        return self.string_path[0] 
    
    def get_last_arival(self):
        """
        :return datetime: last flight arrival
        """
        return None if len(self.path) == 0 else self.path[-1].arrival
    
    def get_flights_path(self): 
        """
        :return str: all the flight numbers of the path separated by a '-'
        """
        return '-'.join(flight.flight_number for flight in self.path)
    
    def get_airport_path(self):
        """
        :return str: all the airport codes of the path separated by a '-'
        """
        return '-'.join(self.string_path)
    
    def get_info(self, _format = "dict"):
        """
        :param str _format: fomat to return the info |'csv'|'dict'|
        :return any: data of the object with the asked format 
        """
        data = {
            'airports': self. get_airport_path(),
            'flights': self.get_flights_path(),
            'total_time': (self.path[-1].arrival - self.path[0].departure),
            'waiting_time': self.waiting_time,
            'transfers': len(self.path)-1,
            'bags_allowed': self.max_bags,
            'price': self.price,
            'bag_price': self.bag_price
        }

        if _format == "csv":
            return ','.join( [str(v) for v in data.values()])
        else:
            return data

    def __str__(self):
        return self.get_info(_format="csv")

    @staticmethod
    def get_headers():
        """
        :return str: headers for outputing ths class as a csv file
        """
        return ','.join(['flights','airports','total_time','waiting_time','transfers','bags_allowed','price','bag_price'])
