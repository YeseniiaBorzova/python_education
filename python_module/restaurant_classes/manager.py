"""Module containing manager representing entity"""

from time import sleep

from human import Human


class Manager(Human):
    """Class representing manager"""
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
        return f"Name:{self.get_name()}, {self.get_surname()}(manager)"

    def get_salary(self) -> float:
        """:return salary of the manager"""
        return self._salary

    @staticmethod
    def manage_problems():
        """static method imitating problem solving process"""
        print("Searching for problems...")
        sleep(1)
        print("Solving problems...")
        sleep(1)
        print("Problems solved!")
