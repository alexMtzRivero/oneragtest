class Flight():

    def __init__(self,source,destination,departure,arrival,flight_number,price,bags_allowed,bag_price):
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.flight_number = flight_number
        self.price = price
        self.bags_allowed = bags_allowed
        self.bag_price = bag_price
                
    def __str__(self):
        return "personalizado"