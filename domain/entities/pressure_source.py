
from abc import ABC, abstractmethod

from domain.value_objects.pressure import Pressure
from domain.entities.source import Source


class PressureSource(Source, ABC):
    @abstractmethod
    def get_current(self) -> Pressure:
        pass
