import logging

class QPXRequestLauncher:

    def __init__(self):
        logging.basicConfig(filename='qpx.log',level=logging.DEBUG)

    def launch_request(self, schedule):
        headers = {'content-type': 'application/json'}
        requests = self.build_requests(schedule, 50)
        #logging.info(data)
        #r = requests.post('https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + self.key,
        #                 data = json.dumps(data),
        #              headers = headers)
        #logging.info(r)

        #jsonResponse = r.json()
        #logging.info(jsonResponse)
        #return jsonResponse
        return ""
