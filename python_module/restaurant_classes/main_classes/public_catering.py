"""Module containing base class representing any public catering place"""
from main_classes.building import Building


class PublicCatering(Building):
    """Class representing place for public eating"""
    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            self._menu = kwargs.get('menu', "Public catering place must have menu")
            self._name = kwargs.get('name', "Public catering place must have name")
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
