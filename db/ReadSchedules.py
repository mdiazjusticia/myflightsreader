from pymongo import MongoClient

class ReadSchedules:

    def __init__(self):
        client = MongoClient()
        self.db = client.flights.schedules


    def get_schedules(self):
        schedules = self.db.find({})
        return schedules

