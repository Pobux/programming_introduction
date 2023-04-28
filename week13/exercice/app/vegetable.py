import datetime

class Vegetable():
    def __init__(self):
        self.planting_date = datetime.datetime.now()
        self.days_to_mature = None
        self.days_to_sprout = None
        self.height = None
        self.days_to_mature = None

    def date_to_mature(self):
        return self.planting_date + datetime.timedelta(days=self.days_to_mature)
