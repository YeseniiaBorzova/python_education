"""Module representing customer entity"""

from human import Human


class Customer(Human):
    """Class represented customer"""
    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            if 'phone_number' in kwargs:
                self._phone_number = kwargs["phone_number"]
            else:
                raise ValueError("Phone number cannot be empty")
            super().__init__(**kwargs)

    def __str__(self):
        """to string"""
        return f"Phone number:{self._phone_number}, name:{self.get_name()} {self.get_surname()}"

    def get_phone_number(self) -> str:
        """:return phone number of the customer"""
        return self._phone_number
