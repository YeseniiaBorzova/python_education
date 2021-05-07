"""This module represents car class inherited
    from base Transport class"""
from transport import Transport


class Car(Transport):
    """Car representing class inherited from base Transport class"""

    _has_engine = True

    def __init__(self, type_of_car: str, model: str,
                 name: str, amount_of_passengers: int, amount_of_wheels: int):
        """Constructor"""

        self._type_of_car = type_of_car
        self._model = model
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Car: " + self._name + ", has engine:" + str(self._has_engine) +\
               ", passengers amount:" + \
               str(self._amount_of_passengers) + ", Model: " + self._model + ", type: " + \
               self._type_of_car + ", amount of wheels: " + str(self._amount_of_wheels)

    def __eq__(self, other):
        """Overriding == operator"""

        if isinstance(other, Car):
            return self._model == other.model and self._type_of_car == other.type_of_car and \
                   self._amount_of_wheels == other.get_amount_of_wheels() and \
                   self._amount_of_passengers == other.get_amount_of_passengers() \
                   and self._name == other.get_name()
        return False

    def __ne__(self, other):
        """Overriding != operator"""

        if isinstance(other, Car):
            return not (self._model == other.model and self._type_of_car == other.type_of_car and
                        self._amount_of_wheels == other.get_amount_of_wheels() and
                        self._amount_of_passengers == other.get_amount_of_passengers()
                        and self._name == other.get_name())
        return True

    def __add__(self, other):
        """Overriding + operator"""

        if isinstance(other, Car):
            return self._name + " " + other.get_name()
        return None

    def __len__(self):
        """Overriding len() that returns length of car name"""

        return len(self._name)

    def __copy__(self):
        """:return a shallow copy of car object"""
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    @staticmethod
    def introduce_self(car_name: str) -> str:
        """:return string that introduces car"""

        return "I am car " + car_name + "!!!"

    @classmethod
    def print_module(cls):
        """prints module name where class is located"""

        print("The name of module where this class is located: ", cls.__module__)

    @property
    def model(self) -> str:
        """:return cars` model"""

        return self._model

    @model.setter
    def model(self, model):
        """sets car model"""

        self._model = model

    @property
    def type_of_car(self) -> str:
        """:return type of car"""

        return self._type_of_car

    @type_of_car.setter
    def type_of_car(self, type_of_car):
        """sets type of car"""
        self._type_of_car = type_of_car

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
