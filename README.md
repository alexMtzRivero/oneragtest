# OneRagTest :rocket:
This is a script created as a solution for a technical test proposed by [OneRagtime](https://www.oneragtime.com). 

### Input
Given a csv file with flight information as follws:   
| source | destination|departure  |arrival | flight_number|price |bags_allowed | bag_price  |
|--|--| -- |-- | -- | -- | -- | -- |
| USM | HKT | 2017-02-11T06:25:00 |2017-02-11T07:25:00|PV404|24|1|9|
|USM|HKT |2017-02-12T12:15:00|2017-02-12T13:15:00|PV755|23|2|9|

Where:
- source, destination are the code of airport the flight is departing from and arriving to 
- departure, arrival are times of departure and arrival 
- price is the price of flight per person (without baggage) 
- bags_allowed the number of bags passenger is allowed to take with them - bag_price additional price per each bag passenger would like to take with them 
- flight_number is the unique identifier of each flight

### Output
This script  **finds all combinations of flights** for the given flight infomation, for passengers **with no bags, one bag or two bags** are able to travel, **having 1 to 4 hours** for each transfer between flights.

The result is presented in csv format with the next information 
| airports| flights | total_time| waiting_time| transfers| bags_allowed| price| bag_price |
|--|--|--|--|--|--|--|--|
|USM-HKT| PV404| 1:00:00| 0:00:00| 0| 1| 24.0| 9.0 |
|USM-HKT| PV755| 1:00:00| 0:00:00| 0| 2| 23.0| 9.0 |
|USM-HKT-USM| PV755-PV634| 4:40:00| 2:45:00| 1| 2| 44.0| 21.0 |

where:
- airports: list of the visited airport codes separated by a '-'
- flights: list of flight numbers in the itinerary separated by a '-'
- total_time: total time of the trip fom fist departure to last arrival
- waiting_time: sum of the time passed waiting betwen transfers
- transfers: number of transfers in the itinerary
- bags_allowed: maximum number of bags alowed in the itinerary
- price: total price of all the flights 
- bag_price: price of carring 1 bag the whole itinerary


## tests
To test this script you can run the next command:
> cat test_data/input.csv | python3 find_combinations.py > result.txt 

The test_data contains the next chases:
 - input.csv: the default input provided by OneRagTime
 - min.csv: just the headers with no data
 - corrupt.csv : not valid input.
 - test.csv: little hand made graph to test 

Feel free to add new test chases :relaxed: