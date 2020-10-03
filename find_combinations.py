import sys, copy
from datetime import datetime, timedelta 
from Models.flight import Flight 
from Models.itinerary import Itinerary
def read_input():
    """
    Reads a flights csv file from a shell pipe and returns a formated dictionary 
    with: 
        airport code as key and,
        a list of flights going out from this airport as the value. 
        
    :return:{ 
            source_airport_code:[flight,...],
            source_airport_code:[flight,...],
            ... 
            }
    """
    departure_airports = {}
    line_count = 0
    #read input
    for line in sys.stdin:
        if line_count == 0:
            #do stuff with the csv headers if you want
            line_count+=1
        else:
            #removes whitespace and end line characters "\n" "\r"
            line = line.rstrip()
            #creates flight object with csv data 
            flight = Flight(*line.split(','))
            
            #format data
            if flight.source not in departure_airports:
               departure_airports[flight.source] = {}
            if flight.destination not in departure_airports[flight.source]:
               departure_airports[flight.source][flight.destination] = [] 
            
            departure_airports[flight.source][flight.destination].append(flight)
    return departure_airports



def get_combinations_of(airports,code_from,_itinerary,itineraries,bags = 0, min_transfer = 1, max_transfer = 4):
        #if this airport has no departures
        if code_from not in airports:
           return itineraries    
        for code_to in airports[code_from]: 
            for flight in airports[code_from][code_to]:
                itinerary = copy.deepcopy(_itinerary)
                bags_allowed = bags <= flight.bags_allowed
                on_time = itinerary.is_on_time_for(flight.departure,min_transfer,max_transfer)
                if bags_allowed and on_time:
                    visited = code_to in itinerary.path
                    if not visited:
                        itinerary.add(flight)
                        itineraries.append(itinerary)
                        itineraries = get_combinations_of(airports,code_to,itinerary,itineraries,bags, min_transfer, max_transfer)
                    #if we end at the beginig it still counts
                    elif itinerary.get_origin() == code_to:
                        itinerary.add(flight)
                        itineraries.append(itinerary)
    
        return itineraries
                

                

def main():
    airports = read_input()
    departure = "C"
    itinerary = Itinerary(departure)
    itineraries = get_combinations_of(airports,departure,itinerary,[],bags=2)
    a,b = datetime.strptime("2017-02-11T06:25:00","%Y-%m-%dT%H:%M:%S" ) , datetime.strptime("2017-02-11T07:25:00","%Y-%m-%dT%H:%M:%S")
    print((b-a) > timedelta(hours=1))
    for i in itineraries:
        print(i)

                   

if __name__ == "__main__":
    main()