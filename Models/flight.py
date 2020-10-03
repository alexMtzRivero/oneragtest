from datetime import datetime
class Flight():

    def __init__(self,source,destination,departure,arrival,flight_number,price,bags_allowed,bag_price):
        self.source = source
        self.destination = destination
        self.departure = datetime.strptime(departure,"%Y-%m-%dT%H:%M:%S") 
        self.arrival = datetime.strptime(arrival,"%Y-%m-%dT%H:%M:%S")
        self.flight_number = flight_number
        self.price = float(price)
        self.bags_allowed = int(bags_allowed)
        self.bag_price = float(bag_price)
                