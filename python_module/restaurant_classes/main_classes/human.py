"""Module containing base class representing human entity"""

from datetime import datetime


class Human:
    """Base class representing human"""
    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:

            self._birthdate = datetime.date(datetime.strptime(kwargs.get('birthdate', "Human must have birthdate"),
                                                              "%d-%m-%Y"))
            self._name = kwargs.get('name', "Human must have name")
            self._surname = kwargs.get('surname', "Human must have surname")
            self._gender = kwargs.get('gender', "Human must have gender")

    def __str__(self):
        """to string"""
        return f"Name:{self._name}, {self._surname}"

    def get_birthdate(self) -> datetime.date:
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
