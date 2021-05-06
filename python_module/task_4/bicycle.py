""" This module represents bicycle class inherited
    from base Transport class"""
from transport import Transport


class Bicycle(Transport):
    """Bicycle representing class inherited from Transport"""

    _has_engine = False

    def __init__(self, type_of_bicycle: str, name: str, amount_of_passengers: int, amount_of_wheels: int):
        """Constructor"""

        self._type_of_bicycle = type_of_bicycle
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Bike: " + self._name + ", has engine:" + str(self._has_engine) + ", passengers amount:" + \
               str(self._amount_of_passengers) + ", type: " + self._type_of_bicycle + \
               "amount of wheels: " + str(self._amount_of_wheels)

    def get_bicycle_type(self) -> str:
        """:return type of particular a bicycle"""

        return self._type_of_bicycle

    def get_name(self) -> str:
        """:return name of particular a bicycle"""

        return self._name

    def get_amount_of_passengers(self) -> int:
        """:return amount of passengers of a particular bicycle"""

        return self._amount_of_passengers

    def get_amount_of_wheels(self) -> int:
        """:return amount of wheels of a particular bicycle"""

        return self._amount_of_wheels
