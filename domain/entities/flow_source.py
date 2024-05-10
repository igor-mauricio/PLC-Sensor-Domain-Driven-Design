
from abc import ABC, abstractmethod

from domain.value_objects.flow import Flow
from domain.entities.source import Source


class FlowSource(Source, ABC):
    @abstractmethod
    def get_current(self) -> Flow:
        pass
