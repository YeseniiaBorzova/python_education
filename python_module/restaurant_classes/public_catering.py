"""Module containing base class representing any public catering place"""
from building import Building


class PublicCatering(Building):
    """Class representing place for public eating"""
    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            if 'menu' in kwargs:
                self._menu = kwargs['menu']
            else:
                raise ValueError("Menu cannot be empty")
            if 'name' in kwargs:
                self._name = kwargs['name']
            else:
                raise ValueError("Name cannot be empty")
            super().__init__(**kwargs)

    def get_menu(self) -> dict:
        """:return menu of the public catering place"""
        return self._menu

    def set_menu(self, menu: dict):
        """setting menu of the public catering place"""
        self._menu = menu

    def get_name(self) -> str:
        """:return name of a public catering"""
        return self._name
