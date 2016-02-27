import json
import requests
from datetime import datetime
from datetime import timedelta

class RequestLauncher:

    def __init__(self):
        self.key = 'XXXXXXXXXXX'

    def build_request(self, schedule):
        trip_duration = schedule['min_duration']
        return_date = datetime.strptime(schedule['date_from'], "%Y-%m-%d") + timedelta(days=trip_duration)
        return_date_string = `return_date.year` + "-" + `return_date.month` + "-" + `return_date.day`
        data = {
          "request": {
            "slice": [
              {
                "origin": schedule['origin'],
                "destination": schedule['destination'],
                "date": schedule['date_from']
              },
              {
                "origin": schedule['destination'],
                "destination": schedule['origin'],
                "date": return_date_string
              }
            ],
            "passengers": {
              "adultCount": 1
            },
            "solutions": 50
          }
        }
        return data

    def launch_request(self, schedule):
        headers = {'content-type': 'application/json'}
        data = self.build_request(schedule)

        print data
        print "aaa"
        #r = requests.post('https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + self.key,
        #                 data = json.dumps(data),
        #                headers = headers)

        #jsonResponse = r.json()
        #print jsonResponse