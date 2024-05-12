from dataclasses import dataclass
from domain.primitives.entity_id import EntityId


@dataclass(frozen=True)
class Entity:
    id: EntityId
