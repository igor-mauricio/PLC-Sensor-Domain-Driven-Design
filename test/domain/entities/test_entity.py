import uuid

import pytest

from domain.primitives.entity import Entity
from domain.primitives.entity_id import EntityId


def test_ids_should_be_the_same_with_same_uuid() -> None:
    id_uuid = uuid.uuid4()
    entity_id = EntityId(id_uuid)
    another_entity_id = EntityId(id_uuid)

    assert entity_id == another_entity_id


def test_entities_should_be_the_same_with_same_id() -> None:
    id_uuid = uuid.uuid4()
    entity_id = EntityId(id_uuid)

    entity1 = Entity(entity_id)
    entity2 = Entity(entity_id)

    assert entity1 == entity2


def test_entities_should_not_change_id() -> None:
    id_uuid = uuid.uuid4()
    entity_id = EntityId(id_uuid)

    entity1 = Entity(entity_id)
    entity2 = Entity(entity_id)

    with pytest.raises(Exception):
        entity1.id = EntityId(uuid.uuid4())  # type: ignore

    assert entity1 == entity2


def test_should_inherit_id() -> None:
    from domain.primitives.entity_id import EntityId
    from domain.value_objects.plc_id import PlcId
    from domain.value_objects.sensor_id import SensorId

    assert issubclass(PlcId, EntityId)
    assert issubclass(SensorId, EntityId)
    assert issubclass(PlcId, EntityId)
