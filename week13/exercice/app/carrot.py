from app import vegetable

class Carrot(vegetable.Vegetable):
    def __init__(self, days_to_mature):
        vegetable.Vegetable.__init__(self)
        self.days_to_mature = days_to_mature
        self.height = 6

    def __str__(self):
        return "Carrot"

    def __repr__(self):
        return "Carrot"
