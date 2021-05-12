"""This module represents motorcycle class inherited
    from base Transport class"""
from transport import Transport


class Motorcycle(Transport):
    """Motorcycle representing class inherited from base Transport class"""

    _has_engine = True

    def __init__(self, model: str, name: str, amount_of_passengers: int, amount_of_wheels: int):
        """Constructor"""

        self._model = model
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Motorcycle: " + self._name + ", has engine:" + str(self._has_engine) + \
               ", passengers amount:" + \
               str(self._amount_of_passengers) + ", Model: " + self._model + \
               ", amount of wheels: " + str(self._amount_of_wheels)

    def get_motorcycle_model(self) -> str:
        """:return model of particular motorcycle"""

        return self._model

    def get_name(self) -> str:
        """:return name of particular a motorcycle"""

        return self._name

    def get_amount_of_passengers(self) -> int:
        """:return amount of passengers of a particular motorcycle"""

        return self._amount_of_passengers

    def get_amount_of_wheels(self) -> int:
        """:return amount of wheels of a particular motorcycle"""

        return self._amount_of_wheels
