"""Module containing Cleaner representing entity"""

from time import sleep

from human import Human


class Cleaner(Human):
    """Cleaner representing class"""
    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            if 'salary' in kwargs:
                self._salary = float(kwargs['salary'])
            else:
                raise ValueError("Salary cannot be empty")
            super().__init__(**kwargs)

    def __str__(self):
        """to string"""
        return f"Name:{self.get_name()}, {self.get_surname()}(cleaner)"

    @staticmethod
    def clean_all_the_mess():
        """static method imitating cleaning process"""
        print("Searching for dirty dishes or other mess...")
        sleep(1)
        print("Cleaning all...")
