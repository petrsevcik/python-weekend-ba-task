import datetime as dt
import csv
import json
import sys

# Command line example
#python solution.py example/example3.csv ZRW BPZ
#python solution.py example/example2.csv YOT IUQ 2

# exp - [{"flights": [[{"flight_no": "QG688", "origin": "YOT", "destination": "GXV", "departure": "2021-09-01T01:10:00", "arrival": "2021-09-01T05:15:00", "base_price": "128.0", "bag_price": "10", "bags_allowed": "2"}, {"flight_no": "QG809", "origin": "GXV", "destination": "IUQ", "departure": "2021-09-01T07:40:00", "arrival": "2021-09-01T08:50:00", "base_price": "17.0", "bag_price": "10", "bags_allowed": "2"}]], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 185.0, "travel_time": "7:40:00"}, {"flights": [[{"flight_no": "QG688", "origin": "YOT", "destination": "GXV", "departure": "2021-09-04T01:10:00", "arrival": "2021-09-04T05:15:00", "base_price": "128.0", "bag_price": "10", "bags_allowed": "2"}, {"flight_no": "QG809", "origin": "GXV", "destination": "IUQ", "departure": "2021-09-04T07:40:00", "arrival": "2021-09-04T08:50:00", "base_price": "17.0", "bag_price": "10", "bags_allowed": "2"}]], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 185.0, "travel_time": "7:40:00"}, {"flights": [[{"flight_no": "QG688", "origin": "YOT", "destination": "GXV", "departure": "2021-09-09T01:10:00", "arrival": "2021-09-09T05:15:00", "base_price": "128.0", "bag_price": "10", "bags_allowed": "2"}, {"flight_no": "QG809", "origin": "GXV", "destination": "IUQ", "departure": "2021-09-09T07:40:00", "arrival": "2021-09-09T08:50:00", "base_price": "17.0", "bag_price": "10", "bags_allowed": "2"}]], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 185.0, "travel_time": "7:40:00"}, {"flights": [[{"flight_no": "SJ462", "origin": "YOT", "destination": "GXV", "departure": "2021-09-01T01:50:00", "arrival": "2021-09-01T05:55:00", "base_price": "142.0", "bag_price": "14", "bags_allowed": "2"}, {"flight_no": "QG809", "origin": "GXV", "destination": "IUQ", "departure": "2021-09-01T07:40:00", "arrival": "2021-09-01T08:50:00", "base_price": "17.0", "bag_price": "10", "bags_allowed": "2"}]], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 207.0, "travel_time": "7:00:00"}, {"flights": [[{"flight_no": "QG339", "origin": "YOT", "destination": "IUT", "departure": "2021-09-01T18:25:00", "arrival": "2021-09-01T22:45:00", "base_price": "137.0", "bag_price": "10", "bags_allowed": "2"}, {"flight_no": "DX815", "origin": "IUT", "destination": "IUQ", "departure": "2021-09-02T00:10:00", "arrival": "2021-09-02T01:45:00", "base_price": "34.0", "bag_price": "9", "bags_allowed": "1"}]], "bags_allowed": "1", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 209.0, "travel_time": "7:20:00"}, {"flights": [[{"flight_no": "DX288", "origin": "YOT", "destination": "IUT", "departure": "2021-09-01T17:35:00", "arrival": "2021-09-01T21:55:00", "base_price": "160.0", "bag_price": "9", "bags_allowed": "2"}, {"flight_no": "DX815", "origin": "IUT", "destination": "IUQ", "departure": "2021-09-02T00:10:00", "arrival": "2021-09-02T01:45:00", "base_price": "34.0", "bag_price": "9", "bags_allowed": "1"}]], "bags_allowed": "1", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 230.0, "travel_time": "8:10:00"}, {"flights": [[{"flight_no": "SJ109", "origin": "YOT", "destination": "IUT", "departure": "2021-09-01T00:35:00", "arrival": "2021-09-01T04:55:00", "base_price": "139.0", "bag_price": "14", "bags_allowed": "2"}, {"flight_no": "SJ147", "origin": "IUT", "destination": "IUQ", "departure": "2021-09-01T08:45:00", "arrival": "2021-09-01T10:20:00", "base_price": "44.0", "bag_price": "14", "bags_allowed": "2"}]], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 239.0, "travel_time": "9:45:00"}, {"flights": [{"flight_no": "QG112", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-01T12:20:00", "arrival": "2021-09-01T17:35:00", "base_price": "238.0", "bag_price": "10", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 258.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "QG112", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-02T12:20:00", "arrival": "2021-09-02T17:35:00", "base_price": "238.0", "bag_price": "10", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 258.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "QG112", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-06T12:20:00", "arrival": "2021-09-06T17:35:00", "base_price": "238.0", "bag_price": "10", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 258.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "QG112", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-11T12:20:00", "arrival": "2021-09-11T17:35:00", "base_price": "238.0", "bag_price": "10", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 258.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "SJ461", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-01T00:10:00", "arrival": "2021-09-01T05:25:00", "base_price": "233.0", "bag_price": "14", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 261.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "SJ461", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-04T00:10:00", "arrival": "2021-09-04T05:25:00", "base_price": "233.0", "bag_price": "14", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 261.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "SJ461", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-09T00:10:00", "arrival": "2021-09-09T05:25:00", "base_price": "233.0", "bag_price": "14", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 261.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "DX418", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-01T23:05:00", "arrival": "2021-09-02T04:20:00", "base_price": "245.0", "bag_price": "9", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 263.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "DX418", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-04T23:05:00", "arrival": "2021-09-05T04:20:00", "base_price": "245.0", "bag_price": "9", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 263.0, "travel_time": "5:15:00"}, {"flights": [{"flight_no": "DX418", "origin": "YOT", "destination": "IUQ", "departure": "2021-09-09T23:05:00", "arrival": "2021-09-10T04:20:00", "base_price": "245.0", "bag_price": "9", "bags_allowed": "2"}], "bags_allowed": "2", "bags_count": 2, "destination": "IUQ", "origin": "YOT", "total_price": 263.0, "travel_time": "5:15:00"}]

class FlightDatabase():

    def __init__(self, file):
        self.file = file

    def load_flights(self):
        "loading flights from csv to nested list"
        flights = []
        with open(self.file, "r") as fl:
            fl_reader = csv.reader(fl)
            for flight in fl_reader:
                flights.append(flight)
        flights.pop(0)
        flights.sort(key=lambda x: x[3])
        return flights

    def is_connecting(self, flight1, flight2):
        "detecting if two flights are connecting"
        if flight1[2] == flight2[1] and flight1[1] != flight2[2]:
            return True
        return False

    def layover_time(self, flight1, flight2):
        "counting time window between two flights"
        td1 = dt.datetime.strptime(flight1[4], '%Y-%m-%dT%H:%M:%S')
        td2 = dt.datetime.strptime(flight2[3], '%Y-%m-%dT%H:%M:%S')
        delta = td2 - td1
        if dt.timedelta(minutes=59) < delta < dt.timedelta(hours=6, minutes=1):  # must be more than 1 hour, less than 6
            return True
        return False

    def make_one_stop_combinations(self, flights):
        "making one stop combinations A -> B -> C"
        combinations = []
        for flight1 in flights:
            for flight2 in flights:
                if self.is_connecting(flight1, flight2) and self.layover_time(flight1, flight2):
                    new_route = flight1, flight2
                    combinations.append(new_route)
        return combinations


class FormattingFlights():

    def __init__(self, bags=0):
        self.bags = bags

    def format_flight(self, flight):
        "format flight data from json"
        formatted_flight = {"flight_no": flight[0],
                            "origin": flight[1],
                            "destination": flight[2],
                            "departure": flight[3],
                            "arrival": flight[4],
                            "base_price": flight[5],
                            "bag_price": flight[6],
                            "bags_allowed": flight[7]}
        return formatted_flight

    def format_itinerary(self, flight):
        "format whole itinerary"
        departure = dt.datetime.strptime(flight[3], '%Y-%m-%dT%H:%M:%S')
        arrival = dt.datetime.strptime(flight[4], '%Y-%m-%dT%H:%M:%S')
        travel_time = str(arrival - departure)

        total_price = float(flight[5]) + (float(flight[6]) * float(self.bags))

        response = {
            "flights": [self.format_flight(flight)],
            "bags_allowed": flight[7],
            "bags_count": self.bags,
            "destination": flight[2],
            "origin": flight[1],
            "total_price": total_price,
            "travel_time": travel_time
        }

        return response

    def formatting_one_stop_flights(self, list_of_flights):
        return [self.format_flight(flight) for flight in list_of_flights]

    def format_itinerary_combo(self, flight_tuples):
        flight1, flight2 = flight_tuples

        departure = dt.datetime.strptime(flight1[3], '%Y-%m-%dT%H:%M:%S')
        arrival = dt.datetime.strptime(flight2[4], '%Y-%m-%dT%H:%M:%S')
        travel_time = str(arrival - departure)

        total_price = float(flight1[5]) + float(flight2[5]) + ((float(flight1[6]) + float(flight2[6])) * float(self.bags))
        x = list(flight_tuples)

        response = {
            "flights": [self.formatting_one_stop_flights(x)],
            "bags_allowed": flight1[7] if flight1[7] <= flight2[7] else flight2[7],
            "bags_count": self.bags,
            "destination": flight2[2],
            "origin": flight1[1],
            "total_price": total_price,
            "travel_time": travel_time
        }
        return response


def validate_one_way(flight, src, dst):
    if flight[1] == src and flight[2] == dst:
        return True


def validate_combo(tuples, src, dst):
    flight1, flight2 = tuples
    if flight1[1] == src and flight2[2] == dst:
        return True


def solution(file, src, dst, bags=0):
    flights = FlightDatabase(file)
    one_way_database = flights.load_flights()
    one_stop_database = flights.make_one_stop_combinations(one_way_database)

    search = []

    for flight in one_way_database:
        if validate_one_way(flight, src, dst):
            result = FormattingFlights(bags)
            search.append(result.format_itinerary(flight))

    for combo in one_stop_database:
        if validate_combo(combo, src, dst):
            result = FormattingFlights(bags)
            search.append(result.format_itinerary_combo(combo))

    sorted_response = sorted(search, key=lambda k: k['total_price'])

    return len(sorted_response)

# csv_file = sys.argv[1]
# origin = sys.argv[2]
# destination = sys.argv[3]
# try:
#     bags = sys.argv[4]
# except IndexError:
#     bags = 0

if __name__ == "__main__":
    print(solution("example/example3.csv", "ZRW", "BPZ" ))



