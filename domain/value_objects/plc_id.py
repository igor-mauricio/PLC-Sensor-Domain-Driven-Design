from dataclasses import dataclass
import uuid
from domain.exceptions import EmptyPlcIdException


@dataclass(frozen=True)
class PlcId:
    id: uuid.UUID

    def __post_init__(self) -> EmptyPlcIdException:
        if self.id == None or self.id == "":
            raise EmptyPlcIdException()

    def __str__(self):
        return str(self.id)

    def __eq__(self, other):
        return str(self.id) == str(other.id)
