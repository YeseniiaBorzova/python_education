"""Module for testing work of created classes"""

from main_classes.restaurant import Restaurant
from main_classes.order import Order
from main_classes.waiter import Waiter
from main_classes.manager import Manager
from main_classes.cleaner import Cleaner
from main_classes.singer import Singer
from main_classes.customer import Customer


def main():
    """function for testing all created classes"""

    # menu of the restaurant
    menu_dict = {"Fried potato": 80, "Grilled salmon": 170, "Grilled vegetables": 100,
                 "Grilled chicken breasts": 120, "Grilled pork": 150, "Juice": 30,
                 "Shrimp salad": 185, "Cheeseburger": 50, "Hamburger": 40, "Sauce": 20,
                 "Cesar with chicken": 100, "Coffee": 45, "Tea": 35, "Olivye salad": 70}

    # manager of the restaurant
    alena_manager = Manager(name="Alena", surname="Bobrova", gender="F",
                            birthdate="23-04-2000", salary=20000)

    # customers of the restaurant
    oleg_customer = Customer(name="Oleg", surname="Jernov", gender="M",
                             phone_number="+380967245911", birthdate="14-09-1991")
    semen_customer = Customer(name="Semen", surname="Kovalenko", gender="M",
                              phone_number="+380663457892", birthdate="02-08-2004")
    sergey_customer = Customer(name="Sergey", surname="Orlov", gender="M",
                               phone_number="+380456783428", birthdate="04-11-1982")
    alina_customer = Customer(name="Alina", surname="Lutenko", gender="F",
                              phone_number="+38074568238", birthdate="07-01-1985")
    maria_customer = Customer(name="Maria", surname="Stolyarova", gender="F",
                              phone_number="+380889314567", birthdate="30-08-2001")
    maxim_customer = Customer(name="Maxim", surname="Karpenko", gender="M",
                              phone_number="+380567812361", birthdate="28-06-1973")

    # customers orders
    oleg_order = Order(customer=oleg_customer,
                       ordered_food={"Grilled salmon": 170, "Grilled vegetables": 100, "Juice": 30},
                       amounts_of_ordered_food=[1, 1, 2])
    maxim_order = Order(customer=maxim_customer, ordered_food=
                        {"Cheeseburger": 50, "Fried potato": 80},
                        amounts_of_ordered_food=[3, 2])
    alina_order = Order(customer=alina_customer, ordered_food={"Shrimp salad": 185, "Coffee": 45},
                        amounts_of_ordered_food=[1, 1])
    maria_order = Order(customer=maria_customer, ordered_food=
                        {"Grilled pork": 150, "Olivye salad": 70, "Cesar with chicken": 100},
                        amounts_of_ordered_food=[2, 1, 1])
    semen_order = Order(customer=semen_customer, ordered_food=
                        {"Grilled vegetables": 100, "Cesar with chicken": 100,
                         "Hamburger": 40, "Sauce": 20, "Fried potato": 80},
                        amounts_of_ordered_food=[2, 1, 2, 1, 2])

    # waiters of the restaurant
    anna_waiter = Waiter(name="Anna", surname="Nosova", gender="F",
                         birthdate="01-05-1998", salary=15000)
    aleksey_waiter = Waiter(name="Aleksey", surname="Shuvalov", gender="M",
                            birthdate="07-07-2002", salary=15000)
    matvey_waiter = Waiter(name="Matvey", surname="Ruban", gender="M",
                           birthdate="15-05-2000", salary=15000)
    valentina_waiter = Waiter(salary=15000, name="Valentina", surname="Semenova",
                              birthdate="02-11-1999", gender="F",
                              orders_to_bring=[semen_order, maria_order],
                              customers_to_bring=[semen_customer, maria_customer])

    # singer in the restaurant
    lera_singer = Singer(salary=17000, song_list=
                         ["Only one who knows", "Cornerstone", "Sweat dreams", "R u mine"],
                         name="Valeria", surname="Solovyova", birthdate="14-12-1992", gender="F")

    # cleaners in the restaurant
    angelina_cleaner = Cleaner(salary=14000, name="Angelina", surname="Lebneva",
                               birthdate="25-03-1995", gender="F")
    georgiy_cleaner = Cleaner(salary=14000, name="Georgiy", surname="Drozdov",
                              birthdate="10-11-1982", gender="M")

    # create a restaurant with all defined above objects
    sierra_restaurant = Restaurant(length=100, width=50, height=3,
                                   address="Mira str 32", name="Sierra",
                                   menu=menu_dict, customers=
                                   [semen_customer, sergey_customer, maxim_customer,
                                    maria_customer, alina_customer, oleg_customer],
                                   managers=[alena_manager],
                                   singer=lera_singer,
                                   cleaners=[angelina_cleaner, georgiy_cleaner],
                                   waiters=[anna_waiter, aleksey_waiter,
                                            matvey_waiter, valentina_waiter],
                                   orders=[oleg_order, maria_order, maxim_order, alina_order])

    sierra_restaurant.entertain_customers()
    print("\n")

    for order in sierra_restaurant.get_orders_list():
        sierra_restaurant.bring_all_the_orders(order)

    print("\n")
    sierra_restaurant.clean_all(georgiy_cleaner)


if __name__ == "__main__":
    main()
