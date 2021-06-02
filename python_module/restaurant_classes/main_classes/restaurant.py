"""Module containing restaurant entity"""
import random

from main_classes.public_catering import PublicCatering
from main_classes.order import Order


class Restaurant(PublicCatering):
    """Class representing restaurant"""
    _customers = []
    _waiters = []
    _managers = []
    _cleaners = []
    _singer = None
    _orders = []

    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            self._customers = kwargs.get('customers', "Restaurant must have customers")
            self._waiters = kwargs.get('waiters', "Restaurant must have waiters")
            self._managers = kwargs.get('managers', "Restaurant must have managers")
            self._cleaners = kwargs.get('cleaners', "Restaurant must have cleaners")
            self._singer = kwargs.get('singer')
            self._orders = kwargs.get('orders')
            super().__init__(**kwargs)

    def __str__(self):
        """to string"""
        return f"In restaurant {self.get_name()} works:\n{len(self._cleaners)}-cleaners" \
               f"\n{len(self._singer)}-singer \n{len(self._waiters)}-waiters\n" \
               f"{len(self._managers)}-mangers \nand have\n{len(self._customers)}-customers"

    def get_customers_list(self) -> list:
        """:return list of customers of the restaurant"""
        return self._customers

    def get_customer(self, customer):
        """:return customer if it is present in this particular restaurant"""
        if customer in self._customers:
            return customer
        return "No such customer in the restaurant"

    def get_waiters_list(self) -> list:
        """:return list of waiters of the restaurant"""
        return self._waiters

    def get_waiter(self, waiter):
        """:return waiter if it is present in this particular restaurant"""
        if waiter in self._waiters:
            return waiter
        return "No such waiter in the restaurant"

    def get_managers_list(self) -> list:
        """:return list of managers of the restaurant"""
        return self._managers

    def get_manager(self, manager):
        """:return manager if it is present in this particular restaurant"""
        if manager in self._managers:
            return manager
        return "No such manager in the restaurant"

    def get_cleaners_list(self) -> list:
        """:return list of cleaners of the restaurant"""
        return self._cleaners

    def get_cleaner(self, cleaner):
        """:return cleaner if it is present in this particular restaurant"""
        if cleaner in self._cleaners:
            return cleaner
        return "No such cleaner in the restaurant"

    def get_orders_list(self) -> list:
        """:return list of orders of the restaurant"""
        return self._orders

    def get_singer(self):
        """:return singer that works in this restaurant"""
        return self._singer

    def set_singer(self, singer):
        """setting singer of the restaurant"""
        self._singer = singer

    def append_customer(self, customer):
        """adding customer to the customer list of the restaurant"""
        self._customers.append(customer)

    def append_waiter(self, waiter):
        """adding waiter to the waiter list of the restaurant"""
        self._waiters.append(waiter)

    def append_manager(self, manager):
        """adding manager to the manager list of the restaurant"""
        self._managers.append(manager)

    def append_cleaner(self, cleaner):
        """adding cleaner to the cleaner list of the restaurant"""
        self._cleaners.append(cleaner)

    def append_order(self, order):
        """adding order to the order list of the restaurant"""
        self._orders.append(order)

    def create_an_order(self, ordered_food, amounts_ordered_food, customer, **kwargs):
        """creating a new order and adding it to the order list"""
        if kwargs is not None:
            if 'waiter' in kwargs:
                new_order = Order(customer=customer, ordered_food=ordered_food,
                                  amounts_of_ordered_food=amounts_ordered_food,
                                  waiter=kwargs['waiter'])
                self.append_order(new_order)
        new_order = Order(customer=customer, ordered_food=ordered_food,
                          amounts_of_ordered_food=amounts_ordered_food)
        self.append_order(new_order)

    def set_order_to_waiter(self, order, waiter):
        """setting order to orders list of waiter"""
        if waiter in self._waiters and order in self._orders:
            waiter.set_order(order)

    def set_customer_to_waiter(self, customer, waiter):
        """setting customer to customers list of waiter"""
        if waiter in self._waiters and customer in self._customers:
            waiter.set_customer(customer)

    def manage_problems(self, manager):
        """calling manage"""
        if manager in self._managers:
            manager.manage_problems()

    def clean_all(self, cleaner):
        """cleans all the mess in the restaurant"""
        if cleaner in self._cleaners:
            cleaner.clean_all_the_mess()

    def entertain_customers(self):
        """chooses a random song to sing to customers"""
        self._singer.sing_a_song()

    def bring_all_the_orders(self, order):
        """chooses a random waiter to bring order to customer"""
        waiter = random.choice(self._waiters)
        print(f"\tWaiter that is assigned this order:{waiter}")
        waiter.take_an_order(order)

