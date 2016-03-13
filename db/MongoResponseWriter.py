from pymongo import MongoClient
import json

class MongoResponseWriter:

    def saveResponse(self, response):
        client = MongoClient()
        db = client.flights.responses
        db.insert(response)