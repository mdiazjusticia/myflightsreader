from SegmentLeg import SegmentLeg
from ItinearySegment import ItinearySegment
from FlightItinerary import FlightItinerary
from Trip import Trip
import time

class QPXResponseParser:



    def parse(self, data):
        trips = data['trips']['tripOption']

        flight_trips = []
        for trip in trips:
            price = trip['saleTotal']
            slices = trip['slice']
            flight_itineraries = []
            for slice in slices: #slice --> itinerary
                duration = slice['duration']
                segments = slice['segment']
                itinerary_segments = []
                for segment in segments: #segment + leg --> leg
                    duration = segment['duration']
                    carrier = segment['flight']['carrier']
                    flight_number = segment['flight']['number']
                    legs = segment['leg']
                    segment_legs = []
                    for leg in legs:
                        origin = leg['origin']
                        destination = leg['destination']
                        duration = leg['duration']
                        aircraft = leg['aircraft']
                        departure_time = leg['departureTime']
                        arrival_time = leg['arrivalTime']
                        segment_leg = SegmentLeg(origin, destination, duration, aircraft, departure_time, arrival_time)
                        segment_legs.append(segment_leg)
                    itinerary_segment = ItinearySegment(carrier, flight_number, duration, segment_legs)
                    itinerary_segments.append(itinerary_segment)
                flight_itineary = FlightItinerary(duration, itinerary_segments)
                flight_itineraries.append(flight_itineary)

            trip = Trip(price, flight_itineraries, time.strftime("%Y-%m-%d"))
            flight_trips.append(trip)

        return flight_trips
