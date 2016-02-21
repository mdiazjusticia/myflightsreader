class SegmentLeg:

    def __init__(self, origin, destination, duration, aircraft, dep_time, arr_time):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.aircraft = aircraft
        self.dep_time = dep_time
        self.arr_time = arr_time

    def to_json(self):
        return dict(origin=self.origin, destination = self.destination, duration = self.duration, aircraft = self.aircraft
                    , dep_time = self.dep_time, arr_time = self.arr_time
                    )
