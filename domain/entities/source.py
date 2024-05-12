from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class Source(ABC):
    @abstractmethod
    def get_current(self):
        pass
