from dataclasses import dataclass
import uuid
from domain.exceptions import EmptySensorIdException
from domain.primitives.entity_id import EntityId


@dataclass(frozen=True)
class SensorId(EntityId):
    id: uuid.UUID

    def __post_init__(self) -> None:
        if id is None or id == "":
            raise EmptySensorIdException()

    def __str__(self):
        return str(self.id)

    def __eq__(self, other):
        return str(self.id) == str(other.id)
