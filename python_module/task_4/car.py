"""This module represents car class inherited
    from base Transport class"""
from transport import Transport


class Car(Transport):
    """Car representing class inherited from base Transport class"""

    _has_engine = True

    def __init__(self, type_of_car: str, model: str, name: str, amount_of_passengers: int, amount_of_wheels: int):
        """Constructor"""

        self._type_of_car = type_of_car
        self._model = model
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Car: " + self._name + ", has engine:" + str(self._has_engine) + ", passengers amount:" + \
               str(self._amount_of_passengers) + ", Model: " + self._model + ", type: " + \
               self._type_of_car + ", amount of wheels: " + str(self._amount_of_wheels)

    def get_car_model(self) -> str:
        """:return model of particular car"""

        return self._model

    def get_type_of_car(self) -> str:
        """:return type of particular car"""

        return self._type_of_car

    def get_name(self) -> str:
        """:return name of particular a car"""

        return self._name

    def get_amount_of_passengers(self) -> int:
        """:return amount of passengers of a particular car"""

        return self._amount_of_passengers

    def get_amount_of_wheels(self) -> int:
        """:return amount of wheels of a particular car"""

        return self._amount_of_wheels

    def get_engine(self) -> bool:
        """:return bool about existence of engine:"""

        return self._has_engine
