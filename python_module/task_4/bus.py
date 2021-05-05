"""This module represents bus class inherited
    from base Transport class"""
from transport import Transport


class Bus(Transport):
    """Bus representing class inherited from base Transport class"""

    has_engine = True

    def __init__(self, length, name, amount_of_passengers, amount_of_wheels):
        """Constructor"""

        self.length = length
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Bus: " + self.name + ", has engine:" + str(self.has_engine) + ", passengers amount:" + \
               str(self.amount_of_passengers) + ", Length(m): " + str(self.length) + \
               ", amount of wheels: " + str(self.amount_of_wheels)

    def get_bus_length(self):
        """:return model of particular bus"""

        return "Bus model: " + self.length

    def get_name(self):
        """:return name of particular a bus"""

        return "Bus: " + self.name

    def get_amount_of_passengers(self):
        """:return amount of passengers of a particular bus"""

        return "Bus amount of passengers: " + self.amount_of_passengers

    def get_amount_of_wheels(self):
        """:return amount of wheels of a particular bus"""

        return "Bus amount of wheels: " + self.amount_of_wheels
