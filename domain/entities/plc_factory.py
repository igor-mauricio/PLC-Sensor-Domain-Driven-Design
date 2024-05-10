import uuid
from domain.entities.plc import Plc
from domain.value_objects.plc_id import PlcId


class PlcFactory:
    @staticmethod
    def default() -> Plc:
        id = uuid.uuid4()
        plc_id = PlcId(id)
        return Plc(plc_id)

    @staticmethod
    def from_id(id: str) -> Plc:
        plc_id = PlcId(id)
        return Plc(plc_id)
