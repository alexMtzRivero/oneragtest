from datetime import timedelta 
class Itinerary():

    def __init__(self,origin_code):
        """
        :param origin_code: String, code of the inital airport  
        """
        self.string_path = [origin_code]
        self.path = []
        self.flight_price = 0
        self.bag_price = 0
        self.max_bags = 0

    def add(self, flight):
        """
        Appends a flight to our path and sums the cost of taking thath flight
        """
        self.string_path.append(flight.destination)
        self.path.append(flight)
        self.flight_price += flight.price
        self.bag_price += flight.bag_price
        if flight.bags_allowed > self.max_bags:
            self.max_bags = flight.bags_allowed

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
            return True
        else:
            dif = departure_time - last_arival
            return dif >= timedelta(hours=min_transfer) and dif <= timedelta(hours=max_transfer)

    def get_origin(self):
        return self.string_path[0] 
    
    def get_last_arival(self):
        return None if len(self.path) == 0 else self.path[-1].arrival
    
    def __str__(self):
        return ','.join(self.string_path) #+ str(self.flight_price)
