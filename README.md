# OneRagTest
This is a script  created as a solution for a technical test

Given a csv file with flight information as follws:   
| source | destination|departure  |arrival | flight_number|price |bags_allowed | bag_price  |
|--|--| -- |-- | -- | -- | -- | -- |
| USM | HKT | 2017-02-11T06:25:00 |2017-02-11T07:25:00|PV404|24|1|9|
|USM|HKT |2017-02-12T12:15:00|2017-02-12T13:15:00|PV755|23|2|9|
,,,,,,
where:
- source, destination are the code of airport the flight is departing from and arriving to 
- departure, arrival are times of departure and arrival 
- price is the price of flight per person (without baggage) 
- bags_allowed the number of bags passenger is allowed to take with them - bag_price additional price per each bag passenger would like to take with them 
- flight_number is the unique identifier of each flight

This script  **finds all combinations of flights** for passengers **with no bags, one bag or two bags** are able to travel, **having 1 to 4 hours** for each transfer between flights. 

## test
> cat test.csv | python3 find_combinations.py > result.txt 