"""Module containing singer entity"""

from human import Human


class Singer(Human):
    """Class representing singer"""
    _song_list = []

    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            if 'salary' in kwargs:
                self._salary = float(kwargs['salary'])
            else:
                raise ValueError("Salary cannot be empty")
            if 'song_list' in kwargs:
                self._song_list = kwargs['song_list']
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
