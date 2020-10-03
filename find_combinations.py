import sys
from Models.flight import Flight 
def read_input():
    """
    Reads a flights csv file from a shell pipe and returns a formated dict 
    with: 
        airport code as key, 
        and a list of flights going out from this airport as the value. 
        
    :return:{ 
            source_airport:[flight,...],
            source_airport:[flight,...],
            ... 
            }
    """
    departure_airports = {}
    line_count = 0
    #read pipe file
    for line in sys.stdin:
        if line_count == 0:
            line_count+=1
            #do stuff with headers if you want
            pass
        else:
            #removes whitespace and end line characters "\n" "\r"
            line = line.rstrip()
            #creates flight object with csv data 
            flight = Flight(*line.split(','))
            #format data
            if flight.source not in departure_airports:
               departure_airports[flight.source] = []
            departure_airports[flight.source].append(flight)

    return departure_airports

def main():
   print(read_input())

                   

if __name__ == "__main__":
    main()