

import random
from domain.value_objects.temperature import Temperature
from domain.entities.temperature_source import TemperatureSource


class TemperatureSourceRandom(TemperatureSource):
    _high = 100
    _low = -100

    def __init__(self, low: int, high: int):
        self._low = low
        self._high = high

    def get_current(self) -> Temperature:
        temp = Temperature(
            random.random() * (self._high - self._low) + self._low)
        return temp
