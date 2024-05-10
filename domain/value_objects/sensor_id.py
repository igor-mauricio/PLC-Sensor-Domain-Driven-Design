from dataclasses import dataclass
import uuid
from domain.exceptions import EmptySensorIdException


@dataclass(frozen=True)
class SensorId:
    id: uuid.UUID

    def __post_init__(self) -> EmptySensorIdException:
        if id == None or id == "":
            raise EmptySensorIdException()

    def __str__(self):
        return str(self.id)

    def __eq__(self, other):
        return str(self.id) == str(other.id)
