from pymongo import MongoClient
import json
import jsonpickle
from ComplexEncoder import ComplexEncoder

class MongoWriter:

    def saveTrips(self, trips):
        client = MongoClient()
        db = client.flights.flights
        #db.insert(trips[0].to_document)
        for trip in trips:
            document = json.dumps(trip.to_json(), cls=ComplexEncoder)
            db.insert(json.loads(document))