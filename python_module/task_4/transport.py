"""This module contains base class Transport"""


class Transport:
    """Class representing base vehicle"""

    def __init__(self, name, amount_of_passengers, amount_of_wheels):
        """Constructor"""

        self.name = name
        self.amount_of_passengers = amount_of_passengers
        self.amount_of_wheels = amount_of_wheels

    def get_name(self):
        """:return name of vehicle"""

        return "Transport name: " + self.name

    def get_amount_of_passengers(self):
        """:return maximum possible amount of passengers"""

        return "Transport max passengers: " + self.amount_of_passengers

    def get_amount_of_wheels(self):
        """:return amount of wheels"""

        return "Transport amount of wheels: " + self.amount_of_wheels
