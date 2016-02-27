class Trip:
    def __init__(self, price, itineraries, date_search):
        self.price = price
        self.itineraries = itineraries
        self.date_search = date_search

    def to_json(self):
        return dict(itineraries=self.itineraries, price=self.price, date_search=self.date_search)
