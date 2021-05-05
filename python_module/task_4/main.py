"""Module for testing functionality of created transport classes"""
from bicycle import Bicycle
from motorcycle import Motorcycle
from car import Car
from bus import Bus


if __name__ == "__main__":
    gt_bicycle = Bicycle(amount_of_wheels=2, amount_of_passengers=1,
                         name="GT", type_of_bicycle="Mountain riding")
    ducati_motorcycle = Motorcycle(amount_of_passengers=1, amount_of_wheels=2,
                                   model="Monster", name="Ducati")
    honda_car = Car(name="Honda", model="Civic type R", type_of_car="Sedan",
                    amount_of_wheels=4, amount_of_passengers=5)
    laz_bus = Bus(name="LAZ695", length=9.2,
                  amount_of_passengers=33, amount_of_wheels=4)

    print(gt_bicycle.__str__())
    print(ducati_motorcycle.__str__())
    print(honda_car.__str__())
    print(laz_bus.__str__())
