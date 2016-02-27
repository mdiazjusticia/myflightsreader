from pymongo import MongoClient
import json
from ComplexEncoder import ComplexEncoder

class MongoWriter:

    def saveTrips(self, trips):
        client = MongoClient()
        db = client.flights.trips
        for trip in trips:
            document = json.dumps(trip.to_json(), cls=ComplexEncoder)
            db.insert(json.loads(document))