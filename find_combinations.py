import sys, copy
from datetime import datetime, timedelta 
from Models.flight import Flight 
from Models.itinerary import Itinerary
## TODO:    
# - format print to CSV and JSON
# - coment code
# - refactor some parts
# - write readme

def read_input():
    """Reads a flights csv file from a shell pipe and returns a formated dictionary  
    
    :return Dict: { 
                'USM':{
                    'HKT':[Flight,...],
                    'DPS':[Flight,...], ...
                },
                from_airport:{
                    to_airport:[Flight,...],
                    to_airport:[Flight,...], ...
                },...
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



def get_combinations_of(segments,code_from,_itinerary,itineraries,bags = 0, min_transfer = 1, max_transfer = 4):
    """Finds all posible paths (itineraries) we can follow from a departure airport given the constrains of
    bags we want to carry, minimum and maximum transef time

    :param Dict segments: formated dictionariy of all the posible flights(see read_input())
    :param str code_from: code of the departure airport we want to check
    :param Itinerary _itinerary: current itinerary that we are following
    :param int bags: bags we want to carry, some filght may not accept more than 1 bag
    :param int min_transfer: minimun time can wait between flights in hours
    :param int max_transfer: maximum time we wait between flights in hours

    :return [Itinerary]: list of all the posible itineraries
    """
    #if this airport has no departures we do nothing
    if code_from not in segments:
        return itineraries  
    #for each airport we can reach from this airport(code_from)  
    for code_to in segments[code_from]:
        #for each flight (same airport destination but diferent departure, price, etc ...) 
        for flight in segments[code_from][code_to]:
            # we create a new itinerary  based on the one that we are following 
            itinerary = copy.deepcopy(_itinerary)
            #check the requirement to take the flight
            bags_allowed = bags <= flight.bags_allowed
            on_time = itinerary.is_on_time_for(flight.departure,min_transfer,max_transfer)
            if bags_allowed and on_time:
                visited = code_to in itinerary.string_path
                if not visited:
                    itinerary.add(flight)
                    itineraries.append(itinerary)
                    #search aigain for the new paths we have from the next airport
                    itineraries = get_combinations_of(segments,code_to,itinerary,itineraries,bags, min_transfer, max_transfer)
                #if we end at the beginig airport we can still go 
                elif itinerary.get_origin() == code_to:
                    itinerary.add(flight)
                    itineraries.append(itinerary)

    return itineraries

def search_all_combinations(segments):
    result = []
    for departure in segments:
        itinerary = Itinerary(departure)
        itineraries = get_combinations_of(segments,departure,itinerary,[])
        result.extend(itineraries)
    return result

def main():
    segments = read_input()
    result = search_all_combinations(segments)
    
    for i in result:
        print(i,file=sys.stdout)

                   
if __name__ == "__main__":
    main()