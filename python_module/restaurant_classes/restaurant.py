"""Module containing restaurant entity"""

from public_catering import PublicCatering
from order import Order


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
            if 'customers' in kwargs:
                self._customers = kwargs['customers']
            else:
                raise ValueError("Restaurant must have customers list")
            if 'waiters' in kwargs:
                self._waiters = kwargs['waiters']
            else:
                raise ValueError("Restaurant must have waiters list")
            if 'managers' in kwargs:
                self._managers = kwargs['managers']
            else:
                raise ValueError("Restaurant must have managers list")
            if 'cleaners' in kwargs:
                self._cleaners = kwargs['cleaners']
            else:
                raise ValueError("Restaurant must have cleaners list")
            if 'singer' in kwargs:
                self._singer = kwargs['singer']
            if 'orders' in kwargs:
                self._orders = kwargs['orders']
            super().__init__(**kwargs)

    def get_customers_list(self) -> list:
        """:return list of customers of the restaurant"""
        return self._customers

    def get_waiters_list(self) -> list:
        """:return list of waiters of the restaurant"""
        return self._waiters

    def get_managers_list(self) -> list:
        """:return list of managers of the restaurant"""
        return self._managers

    def get_cleaners_list(self) -> list:
        """:return list of cleaners of the restaurant"""
        return self._cleaners

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
        """setting order to a waiter"""
        if waiter in self._waiters and order in self._orders:
            waiter.set_order(order)
