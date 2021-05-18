"""Module representing waiter entity"""

from human import Human


class Waiter(Human):
    """Class representing waiter"""
    _orders_to_bring = []
    _customers_to_bring = []

    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            if 'salary' in kwargs:
                self._salary = float(kwargs['salary'])
            else:
                raise ValueError("Salary cannot be empty")
            if 'orders_to_bring' in kwargs:
                self._orders_to_bring = kwargs['orders_to_bring']
            else:
                raise ValueError("Waiter must have a list of orders to bring")
            if 'customers_to_bring' in kwargs:
                self._customers_to_bring = kwargs['customers_to_bring']
            else:
                raise ValueError("Waiter must have a list of customers to which to bring orders")

            super().__init__(**kwargs)

    def set_orders_list(self, order_list):
        """setting list of orders of a waiter"""
        self._orders_to_bring = order_list

    def set_order(self, order):
        """setting order to a waiter"""
        self._orders_to_bring.append(order)

    def set_customers_list(self, customer_list):
        """setting list of customers to the waiter"""
        self._customers_to_bring = customer_list

    def get_salary(self) -> float:
        """:return salary of the waiter"""
        return self._salary

    def take_an_order(self):
        """method imitating taking of order"""
        for order in self._orders_to_bring:
            print(f"Taking order:{order}")

    def bring_order_to_customer(self):
        """method imitating brining orders to customers"""
        for order in self._orders_to_bring:
            for customer in self._customers_to_bring:
                if order.get_customer().get_phone_number() == customer.get_phone_number():
                    print(f"Bringing {order} to customer:{customer}")
