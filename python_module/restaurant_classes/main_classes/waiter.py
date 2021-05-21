"""Module representing waiter entity"""

from main_classes.human import Human


class Waiter(Human):
    """Class representing waiter"""
    _orders_to_bring = []
    _customers_to_bring = []

    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            self._salary = float(kwargs.get('salary', "Salary cannot be empty"))
            self._orders_to_bring = kwargs.get('orders_to_bring', [])
            self._customers_to_bring = kwargs.get('customers_to_bring', [])
            super().__init__(**kwargs)

    def __str__(self):
        """to string"""
        return f"Name:{self.get_name()}, {self.get_surname()}(waiter)"

    def set_orders_list(self, order_list):
        """setting list of orders of a waiter"""
        self._orders_to_bring = order_list

    def set_order(self, order):
        """appending order to order list"""
        self._orders_to_bring.append(order)

    def set_customers_list(self, customer_list):
        """setting list of customers to the waiter"""
        self._customers_to_bring = customer_list

    def set_customer(self, customer):
        """appending customer to customers list"""
        self._customers_to_bring.append(customer)

    def get_salary(self) -> float:
        """:return salary of the waiter"""
        return self._salary

    @staticmethod
    def take_an_order(order):
        """method imitating taking of order"""
        print(f"Taking order:{order}")

    def bring_order_to_customer(self):
        """method imitating brining orders to customers"""
        for order in self._orders_to_bring:
            for customer in self._customers_to_bring:
                if order.get_customer().get_phone_number() == customer.get_phone_number():
                    print(f"Bringing {order} to customer:{customer}")
