"""Module containing singer entity"""

from main_classes.human import Human
from random import choice


class Singer(Human):
    """Class representing singer"""
    _song_list = []

    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            self._salary = float(kwargs.get('salary', "Salary cannot be empty"))
            self._song_list = kwargs.get('song_list', "No songs")
            super().__init__(**kwargs)

    def __str__(self):
        """to string"""
        return f"Name:{self.get_name()}, {self.get_surname()}(singer)"

    def get_salary(self) -> float:
        """:return salary of the singer"""
        return self._salary

    def get_song_list(self) -> list:
        """:return repertoire of a singer"""
        return self._song_list

    def set_song_list(self, song_list):
        """setting repertoire a singer"""
        self._song_list = song_list

    def sing_a_song(self):
        """setting random song for singer to sing"""
        song = choice(self._song_list)
        print(f"Singing song:{song}")
