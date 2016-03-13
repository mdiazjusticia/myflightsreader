from QPXResponseParser import QPXResponseParser
from MongoTripsWriter import MongoTripsWriter
from ReadSchedules import ReadSchedules
from QPXRequestBuilder import QPXRequestBuilder
from QPXRequestLauncher import QPXRequestLauncher
from MongoResponseWriter import MongoResponseWriter

schedules_reader = ReadSchedules();
launcher = QPXRequestLauncher();
builder = QPXRequestBuilder();
response_writer = MongoResponseWriter()
parser = QPXResponseParser()
writer = MongoTripsWriter()



schedules = schedules_reader.get_schedules()
requests = builder.build_requests(schedules)

#for schedule in schedules:
#    response = launcher.build_requests(schedule)
#    flight_trips = parser.parse(response)
#    writer.saveTrips(flight_trips)
#    response_writer.saveResponse(response)