class Trip:
    def __init__(self, price, itineraries):
        self.price = price
        self.itineraries = itineraries

    def to_json(self):
        return dict(itineraries=self.itineraries, price=self.price)
