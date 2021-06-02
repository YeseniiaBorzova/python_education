"""Module containing order entity"""


class Order:
    """Class representing order"""
    _waiter = None

    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            self._customer = kwargs.get('customer', "Order must have customer")
            self._waiter = kwargs.get('waiter')
            self._ordered_food = kwargs.get('ordered_food', "Ordered must have list of ordered positions")
            self._amounts_of_ordered_food = kwargs.get('amounts_of_ordered_food',
                                                       "Order must have amounts of ordered positions")

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
