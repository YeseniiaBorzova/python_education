"""This module represents car class inherited
    from base Transport class"""
from transport import Transport


class Car(Transport):
    """Car representing class inherited from base Transport class"""

    has_engine = True

    def __init__(self, type_of_car, model, name, amount_of_passengers, amount_of_wheels):
        """Constructor"""

        self.type_of_car = type_of_car
        self.model = model
        super().__init__(name, amount_of_passengers, amount_of_wheels)

    def __str__(self):
        """To string method"""

        return "Car: " + self.name + ", has engine:" + str(self.has_engine)+ ", passengers amount:" + \
               str(self.amount_of_passengers) + ", Model: " + self.model + ", type: " + \
               self.type_of_car +", amount of wheels: " + str(self.amount_of_wheels)

    def get_car_model(self):
        """:return model of particular car"""

        return "Car model: " + self.model

    def get_type_of_car(self):
        """:return type of particular car"""

        return "Car type: " + self.type_of_car

    def get_name(self):
        """:return name of particular a car"""

        return "Car: " + self.name

    def get_amount_of_passengers(self):
        """:return amount of passengers of a particular car"""

        return "Car amount of passengers: " + self.amount_of_passengers

    def get_amount_of_wheels(self):
        """:return amount of wheels of a particular car"""

        return "Car amount of wheels: " + self.amount_of_wheels
