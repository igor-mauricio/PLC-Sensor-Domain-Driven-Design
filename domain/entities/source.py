
from abc import ABC, abstractmethod
from typing import TypeVar

from domain.value_objects.flow import Flow

T = TypeVar('T')


class Source(ABC):
    @abstractmethod
    def get_current(self) -> T:
        pass
