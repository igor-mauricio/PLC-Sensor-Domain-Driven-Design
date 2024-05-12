from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar

from domain.value_objects.sensor_id import SensorId
from domain.entities.source import Source

T = TypeVar("T")


@dataclass
class Sensor(ABC):
    id: SensorId
    source: Source

    @abstractmethod
    def measure(self):
        return self.source.get_current()

    @abstractmethod
    def measure_string(self) -> str: ...
