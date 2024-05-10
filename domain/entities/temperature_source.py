
from abc import ABC, abstractmethod

from domain.value_objects.temperature import Temperature
from domain.entities.source import Source


class TemperatureSource(Source, ABC):
    @abstractmethod
    def get_current(self) -> Temperature:
        pass
