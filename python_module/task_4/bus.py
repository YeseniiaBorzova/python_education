"""This module represents bus class inherited
    from base Transport class"""
from transport import Transport


class Bus(Transport):
    """Bus representing class inherited from base Transport class"""

    _has_engine = True

    def __init__(self, length: float, name: str, amount_of_passengers: int, amount_of_wheels: int):
        """Constructor"""

        self._length = length
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Bus: " + self._name + ", has engine:" + str(self._has_engine) + ", passengers amount:" + \
               str(self._amount_of_passengers) + ", Length(m): " + str(self._length) + \
               ", amount of wheels: " + str(self._amount_of_wheels)

    def get_bus_length(self) -> float:
        """:return model of particular bus"""

        return self._length

    def get_name(self) -> float:
        """:return name of particular a bus"""

        return self._name

    def get_amount_of_passengers(self) -> int:
        """:return amount of passengers of a particular bus"""

        return self._amount_of_passengers

    def get_amount_of_wheels(self) -> int:
        """:return amount of wheels of a particular bus"""

        return self._amount_of_wheels
