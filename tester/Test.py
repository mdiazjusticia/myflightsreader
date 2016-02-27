from QPXResponseParser import QPXResponseParser
from MongoWriter import MongoWriter
from ReadSchedules import ReadSchedules
from RequestLauncher import RequestLauncher

schedules_reader = ReadSchedules();
launcher = RequestLauncher();

#with open('../requestBuilder/sample_sample') as data_file:
#    data = json.load(data_file)


schedules = schedules_reader.get_schedules()
for schedule in schedules:
    launcher.launch_request(schedule)


parser = QPXResponseParser()
#flight_trips = parser.parse(data)
writer = MongoWriter()
#writer.saveTrips(flight_trips)