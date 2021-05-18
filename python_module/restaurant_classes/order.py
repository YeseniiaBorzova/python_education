"""Module containing order entity"""


class Order:
    """Class representing order"""
    _waiter = None

    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            if 'customer' in kwargs:
                self._customer = kwargs['customer']
            else:
                raise ValueError("Each order must have its customer")
            if 'waiter' in kwargs:
                self._waiter = kwargs['waiter']
            if 'ordered_food' in kwargs:
                self._ordered_food = kwargs['ordered_food']
            else:
                raise ValueError("Each order must have dict with ordered food")
            if 'amounts_of_ordered_food' in kwargs:
                self._amounts_of_ordered_food = kwargs['amounts_of_ordered_food']
            else:
                raise ValueError("Each order must have amounts of ordered food")

    def __str__(self):
        """to string"""
        return f"Customer:{self._customer}, ordered food:{self._ordered_food}, " \
               f"amounts:{self._amounts_of_ordered_food}"

    def set_waiter(self, waiter):
        """setting waiter to the order"""
        self._waiter = waiter

    def get_customer(self):
        """:return customer associated with order"""
        return self._customer

    def get_ordered_food(self) -> dict:
        """:return dictionary with name of dish and its price"""
        return self._ordered_food

    def calculate_price_of_order(self) -> float:
        """:return price of the order"""
        price_list = []
        for price in self._ordered_food.values():
            price_list.append(price)
        total_price = sum([a*b for a, b in zip(price_list, self._amounts_of_ordered_food)])
        return total_price
