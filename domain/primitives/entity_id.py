from dataclasses import dataclass
import uuid

from domain.exceptions import EmptyEntityIdException


@dataclass(frozen=True)
class EntityId:
    id: uuid.UUID

    def __post_init__(self) -> None:
        if self.id is None or str(self.id) == "":
            raise EmptyEntityIdException()

    def __str__(self):
        return str(self.id)
