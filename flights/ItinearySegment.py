class ItinearySegment:

    def __init__(self, carrier, flight_number, duration, legs):
        self.carrier = carrier
        self.flight_number = flight_number
        self.duration = duration
        self.legs = legs

    def to_json(self):
        return dict(carrier=self.carrier, flight_number = self.flight_number, duration = self.duration, legs = self.legs)
