"""This module contains base class Transport"""


class Transport:
    """Class representing base vehicle"""

    def __init__(self, name: str, amount_of_passengers: int, amount_of_wheels: int):
        """Constructor"""

        self._name = name
        self._amount_of_passengers = amount_of_passengers
        self._amount_of_wheels = amount_of_wheels

    def get_name(self) -> str:
        """:return name of vehicle"""

        return self._name

    def get_amount_of_passengers(self) -> int:
        """:return maximum possible amount of passengers"""

        return self._amount_of_passengers

    def get_amount_of_wheels(self) -> int:
        """:return amount of wheels"""

        return self._amount_of_wheels
