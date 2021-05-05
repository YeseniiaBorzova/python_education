""" This module represents bicycle class inherited
    from base Transport class"""
from transport import Transport


class Bicycle(Transport):
    """Bicycle representing class inherited from Transport"""

    has_engine = False

    def __init__(self, type_of_bicycle, name, amount_of_passengers, amount_of_wheels):
        """Constructor"""

        self.type_of_bicycle = type_of_bicycle
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Bike: " + self.name + ", has engine:" + str(self.has_engine) + ", passengers amount:" + \
               str(self.amount_of_passengers) + ", type: " + self.type_of_bicycle + \
               "amount of wheels: " + str(self.amount_of_wheels)

    def get_bicycle_type(self):
        """:return type of particular a bicycle"""

        return "Bicycle type: " + self.type_of_bicycle

    def get_name(self):
        """:return name of particular a bicycle"""

        return "Bicycle: " + self.name

    def get_amount_of_passengers(self):
        """:return amount of passengers of a particular bicycle"""

        return "Bicycle amount of passengers: " + self.amount_of_passengers

    def get_amount_of_wheels(self):
        """:return amount of wheels of a particular bicycle"""

        return "Bicycle amount of wheels: " + self.amount_of_wheels
