"""Module for testing functionality of created transport classes"""
from copy import copy

from bicycle import Bicycle
from motorcycle import Motorcycle
from car import Car
from bus import Bus
from electric_car import ElectricCar

if __name__ == "__main__":
    gt_bicycle = Bicycle(amount_of_wheels=2, amount_of_passengers=1,
                         name="GT", type_of_bicycle="Mountain riding")
    ducati_motorcycle = Motorcycle(amount_of_passengers=1, amount_of_wheels=2,
                                   model="Monster", name="Ducati")
    honda_car1 = Car(name="Honda", model="Civic type R", type_of_car="Sedan",
                     amount_of_wheels=4, amount_of_passengers=5)
    honda_car2 = Car(name="Honda", model="Civic type R", type_of_car="Sedan",
                     amount_of_wheels=4, amount_of_passengers=5)
    gw_voleex = Car(name="Great Wall", model="Voleex c30", type_of_car="Sedan",
                    amount_of_wheels=4, amount_of_passengers=5)
    laz_bus = Bus(name="LAZ695", length=9.2,
                  amount_of_passengers=33, amount_of_wheels=4)

    bmw_i8 = ElectricCar(name="BMW", model="i8", type_of_car="coupe", amount_of_passengers=2,
                         amount_of_wheels=4, voltage=30, amperage=5)

    # testing
    print(gt_bicycle)
    print(ducati_motorcycle)
    print(honda_car1)
    print(honda_car1 == honda_car2)
    print(honda_car1 + gw_voleex)
    print(laz_bus)
    print(bmw_i8)
    print(honda_car1.model)
    gw_voleex.type_of_car = "Liftback"
    copy_car = copy(honda_car1)
    print(copy_car)
    print(gw_voleex.type_of_car)
    print(len(bmw_i8))
    Car.print_module()
