from pymongo import MongoClient
import json

class ReadSchedules:

    def __init__(self):
        client = MongoClient()
        self.db = client.flights.schedules


    def get_schedules(self):
        schedules = self.db.find({'origin' : 'BCN'})
        return schedules

