from dataclasses import dataclass
import uuid
from domain.exceptions import EmptyPlcIdException
from domain.primitives.entity_id import EntityId


@dataclass(frozen=True)
class PlcId(EntityId):
    id: uuid.UUID

    def __post_init__(self) -> None:
        if self.id is None or self.id == "":
            raise EmptyPlcIdException()

    def __str__(self):
        return str(self.id)

    def __eq__(self, other):
        return str(self.id) == str(other.id)
