import json
from QPXResponseParser import QPXResponseParser
from MongoWriter import MongoWriter

with open('../requestBuilder/json_sample') as data_file:
    data = json.load(data_file)

parser = QPXResponseParser()
flight_trips = parser.parse(data)
writer = MongoWriter()
writer.saveTrips(flight_trips)