"""This module represents motorcycle class inherited
    from base Transport class"""
from transport import Transport


class Motorcycle(Transport):
    """Motorcycle representing class inherited from base Transport class"""

    has_engine = True

    def __init__(self, model, name, amount_of_passengers, amount_of_wheels):
        """Constructor"""

        self.model = model
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Motorcycle: " + self.name + ", has engine:" + str(self.has_engine) + \
               ", passengers amount:" + \
               str(self.amount_of_passengers) + ", Model: " + self.model + \
               ", amount of wheels: " + str(self.amount_of_wheels)

    def get_motorcycle_model(self):
        """:return model of particular motorcycle"""

        return "Motorcycle model: " + self.model

    def get_name(self):
        """:return name of particular a motorcycle"""

        return "Motorcycle: " + self.name

    def get_amount_of_passengers(self):
        """:return amount of passengers of a particular motorcycle"""

        return "Motorcycle amount of passengers: " + self.amount_of_passengers

    def get_amount_of_wheels(self):
        """:return amount of wheels of a particular motorcycle"""

        return "Motorcycle amount of wheels: " + self.amount_of_wheels
