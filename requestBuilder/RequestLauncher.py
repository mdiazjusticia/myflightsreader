import json
import requests

key = 'AIzaSyCEKUxTbWeX0Ef78YoIYV81NY1jKfrn8ac'
data = {
  "request": {
    "slice": [
      {
        "origin": "BCN",
        "destination": "AMS",
        "date": "2016-03-19"
      }
    ],
    "passengers": {
      "adultCount": 1
    },
    "solutions": 20,
    "refundable": False
  }
}
headers = {'content-type': 'application/json'}
r = requests.post('https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + key,
                 data = json.dumps(data),
                headers = headers)

jsonResponse = r.json()
print jsonResponse