"""This module represents electricity class"""


class Electricity:
    """Class representing electricity"""

    _need_fuel = False
    _need_charging = True

    def __init__(self, voltage: float, amperage: float):
        """Constructor"""

        self._voltage = voltage
        self._amperage = amperage

    def __str__(self):
        """To string method"""

        return str(self._voltage) + "V, " + str(self._amperage) + "A."

    def get_voltage(self) -> float:
        """":return voltage of electricity"""

        return self._voltage

    def get_amperage(self) -> float:
        """:return amperage of electricity"""

        return self._amperage

    def get_fuel(self) -> bool:
        """:return bool value about needs in fuel"""

        return self._need_fuel

    def get_charging(self) -> bool:
        """:return bool value about need in charging"""

        return self._need_charging
