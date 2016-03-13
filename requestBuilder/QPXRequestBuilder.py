from datetime import datetime
from datetime import timedelta
import logging
from random import randint
from TripRequest import TripRequest

class QPXRequestBuilder:

    def __init__(self):
        logging.basicConfig(filename='qpx.log', level=logging.DEBUG)
        self.request_limit = 30
        self.request_solutions = 50

    def create_slice(self, origin, destination, date):
        slice = {"origin" : origin, "destination" : destination, "date" : date}
        return slice

    def create_slices(self, schedule, date_ini, trip_duration):
        slices = []
        itinerary_date = date_ini
        schedule_itineraries = schedule['itineraries']
        for itinerary in schedule_itineraries:
            itinerary_date_str = `itinerary_date.year` + "-" + `itinerary_date.month` + "-" + `itinerary_date.day`
            slice = self.create_slice(itinerary['origin'], itinerary['destination'], itinerary_date_str)
            itinerary_date = itinerary_date + timedelta(days=trip_duration)
            slices.append(slice)

        return slices

    def build_request(self, schedule, ini_date, duration):
        slices = self.create_slices(schedule, ini_date, duration)
        passengers = {"adultCount" : 1}
        request = {"slice" : slices, "passengers" : passengers, "solutions" : self.request_solutions}
        data = {"request" : request}
        return data


    def build_requests(self, schedules):
        requests = {}
        n = 0
        total_schedules = schedules.count()
        left = self.request_limit
        num = 1
        for schedule in schedules:
            num_request_schedule = 0
            max_request_schedule = 0
            if num == total_schedules:
                max_request_schedule = left
            else:
                max_request_schedule = min(randint(0, self.request_limit), left)
                left = left - max_request_schedule

            trip_min_duration = schedule['min_duration']
            trip_max_duration = schedule['max_duration']

            ini_date = datetime.strptime(schedule['date_from'], "%Y-%m-%d")
            end_date = datetime.strptime(schedule['date_to'], "%Y-%m-%d")
            diff_date = (end_date - ini_date).days
            while num_request_schedule < max_request_schedule:
                duration_days = randint(trip_min_duration, trip_max_duration)
                offset = randint(0, diff_date)
                trip_date = ini_date + timedelta(days=offset)
                request = self.build_request(schedule, trip_date, duration_days)
                key = self.generate_key(request)
                if requests.get(key) == None:
                    num_request_schedule += 1
                    requests[key] = request

            n = n + num_request_schedule
            num += 1
            if n >= self.request_limit:
                break
        return requests


    def generate_key(self, request):
        key = ""
        for slice in request['request']['slice']:
            key += "/" + slice['origin'] + "-" + slice['destination'] + "-" + slice['date']
        return key