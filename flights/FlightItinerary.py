class FlightItinerary:

    def __init__(self, duration, segments):
        self.duration = duration
        self.segments = segments

    def to_json(self):
        return dict(duration = self.duration, segments = self.segments)
