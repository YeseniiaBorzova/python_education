"""Module containing base class representing any building"""


class Building:
    """Building representing class"""
    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            self._address = kwargs.get('address', "Address cannot be empty")
            self._length = kwargs.get('length', "Length of the building cannot be empty")
            self._width = kwargs.get('width', "Width of the building cannot be empty")
            self._height = kwargs.get('height', "height of the building cannot be empty")

    def get_area_of_a_building(self) -> float:
        """:return area of a building"""
        return self._width*self._length

    def get_volume_of_a_building(self) -> float:
        """:return volume of a building"""
        return self._width*self._length*self._height

    def get_address(self) -> str:
        """:return address of a building"""
        return self._address
