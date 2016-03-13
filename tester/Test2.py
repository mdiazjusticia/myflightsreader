from QPXResponseParser import QPXResponseParser
from MongoTripsWriter import MongoTripsWriter
from ReadSchedules import ReadSchedules
from QPXRequestLauncher import QPXRequestLauncher
from MongoResponseWriter import MongoResponseWriter
import json

launcher = QPXRequestLauncher();
response_writer = MongoResponseWriter()
parser = QPXResponseParser()
writer = MongoTripsWriter()

with open('../requestBuilder/sample/multidestino') as data_file:
    response = json.load(data_file)

flight_trips = parser.parse(response)
writer.saveTrips(flight_trips)
response_writer.saveResponse(response)