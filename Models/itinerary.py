from datetime import timedelta 
class Itinerary():

    def __init__(self,origin_code):
        self.string_path = [origin_code]
        self.path = []
        self.flight_price = 0
        self.bag_price = 0

    def add(self, flight):
        self.string_path.append(flight.destination)
        self.path.append(flight)
        self.flight_price += flight.price
        self.bag_price += flight.bag_price

    def is_on_time_for(self,departure_time,min_transfer, max_transfer):
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
