"""Module representing electric car"""

from car import Car
from electricity import Electricity


class ElectricCar(Car, Electricity):
    """Class describes electric car inherited features from Car and Electricity"""

    def __init__(self, type_of_car: str, model: str, name: str, amount_of_passengers: int,
                 amount_of_wheels: int, voltage: float, amperage: float):
        """Constructor"""

        Car.__init__(self, type_of_car, model, name, amount_of_passengers, amount_of_wheels)
        Electricity.__init__(self, voltage, amperage)

    def __str__(self):
        """To string method"""

        return "Electric car:" + self.get_name() + " " + self.get_car_model() + " " + \
               self.get_type_of_car() + ", Power adapter characteristics(" + \
               str(self.get_voltage()) + "V, " + str(self.get_amperage()) \
               + "A), max passengers: " + str(self.get_amount_of_passengers()) + ", wheels:" \
               + str(self.get_amount_of_wheels()) + ", has engine: " + str(self.get_engine()) \
               + ", needs fuel:" + str(self.get_fuel()) + ", needs charging:" +\
               str(self.get_charging())
