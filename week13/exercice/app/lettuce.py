from app import vegetable

class Lettuce(vegetable.Vegetable):
    def __init__(self, days_to_mature):
        vegetable.Vegetable.__init__(self)
        self.days_to_mature = days_to_mature
        self.height = 4

    def __str__(self):
        return "Lettuce"

    def __repr__(self):
        return "Lettuce"
