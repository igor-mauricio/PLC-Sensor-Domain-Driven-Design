
from abc import ABC, abstractmethod

from application.commands import UserCommand
from domain.entities.plc import Plc


class Presenter(ABC):

    @abstractmethod
    def home(self):
        ...

    @abstractmethod
    def show_plcs(self, plcs: list[Plc]):
        ...

    @abstractmethod
    def show_plc_info(self, plc: Plc):
        ...

    @abstractmethod
    def show_help(self):
        ...

    @abstractmethod
    def show_success(self, message):
        ...

    @abstractmethod
    def show_error(self, message):
        ...

    @abstractmethod
    def show_info(self, message):
        ...

    @abstractmethod
    def exit(self):
        ...

    @abstractmethod
    def get_user_action(self) -> UserCommand:
        ...
