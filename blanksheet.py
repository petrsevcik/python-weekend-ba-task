import datetime as dt
import csv
import json

def load_flights(file):
    "loading flights from csv to nested list"
    flights = []
    with open(file, "r") as fl:
        fl_reader = csv.reader(fl)
        for flight in fl_reader:
            flights.append(flight)
    flights.pop(0)
    flights.sort(key=lambda x: x[3])
    return flights

def format_flight(flight):
    formatted_flight = {"flight_no": flight[0],
                "origin": flight[1],
                "destination": flight[2],
                "departure": flight[3],
                "arrival": flight[4],
                "base_price": flight[5],
                "bag_price": flight[6],
                "bags_allowed": flight[7]}
    return formatted_flight

def format_response(flight, bags=0):

    departure = dt.datetime.strptime(flight[3], '%Y-%m-%dT%H:%M:%S')
    arrival = dt.datetime.strptime(flight[4], '%Y-%m-%dT%H:%M:%S')
    travel_time = str(arrival - departure)

    total_price = float(flight[5]) + (float(flight[6]) * bags)

    response = {
        "flights": [format_flight(flight)],
        "bags_allowed": flight[7],
        "bags_count": bags,
        "destination": flight[2],
        "origin": flight[1],
        "total_price": total_price,
        "travel_time": travel_time
    }

    return response

def solution(file, src, dst, bags=0):
    flights = load_flights(file)
    formatted = []
    for flight in flights:
        x = format_response(flight, bags)
        formatted.append(x)
    sorted_response = sorted(formatted, key=lambda k: k['total_price'])

    search = []
    for fli in sorted_response:
        if fli["destination"] == dst and fli["origin"] == src and int(fli["bags_allowed"]) >= bags:
            search.append(fli)
    return search

x = (solution("example/example1.csv", "DHE", "NRX", 2))
print(json.dumps(x))




