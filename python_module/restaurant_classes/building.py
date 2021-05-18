"""Module containing base class representing any building"""


class Building:
    """Building representing class"""
    def __init__(self, **kwargs):
        """Constructor"""
        if kwargs is not None:
            if 'address' in kwargs:
                self._address = kwargs['address']
            else:
                raise ValueError("Address cannot be empty")
            if 'length' in kwargs:
                self._length = kwargs['length']
            else:
                raise ValueError("Length of the building cannot be empty")
            if 'width' in kwargs:
                self._width = kwargs['width']
            else:
                raise ValueError("Width of the building cannot be empty")
            if 'height' in kwargs:
                self._height = kwargs['height']
            else:
                raise ValueError("height of the building cannot be empty")

    def get_area_of_a_building(self) -> float:
        """:return area of a building"""
        return self._width*self._length

    def get_volume_of_a_building(self) -> float:
        """:return volume of a building"""
        return self._width*self._length*self._height

    def get_address(self) -> str:
        """:return address of a building"""
        return self._address
