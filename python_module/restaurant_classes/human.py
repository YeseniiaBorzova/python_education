"""Module containing base class representing human entity"""

from datetime import datetime


class Human:
    """Base class representing human"""
    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            if 'birthdate' in kwargs:
                self._birthdate = datetime.date(datetime.strptime(kwargs['birthdate'], "%d-%m-%Y"))
            else:
                raise ValueError("Birthdate cannot be empty")
            if 'name' in kwargs:
                self._name = kwargs['name']
            else:
                raise ValueError("Name cannot be empty")
            if 'surname' in kwargs:
                self._surname = kwargs['surname']
            else:
                raise ValueError("Surname cannot be empty")
            if 'gender' in kwargs:
                self._gender = kwargs['gender']
            else:
                raise ValueError("Gender cannot be empty")

    def __str__(self):
        """to string"""
        return f"Name:{self._name}, {self._surname}"

    def get_birthdate(self) -> datetime:
        """:return humans` birthdate"""
        return self._birthdate

    def get_age(self) -> int:
        """:return age of human"""
        today = datetime.today()
        return today.year - self._birthdate.year - ((today.month, today.day) <
                                                    (self._birthdate.month, self._birthdate.day))

    def get_name(self) -> str:
        """:return humans` name"""
        return self._name

    def get_surname(self) -> str:
        """:return humans` surname"""
        return self._surname

    def get_gender(self) -> str:
        """:return humans` gender"""
        return self._gender
