from abc import ABC, abstractmethod

from domain.entities.sensor import Sensor
from domain.value_objects.plc_id import PlcId
from domain.value_objects.sensor_id import SensorId
from domain.entities.plc import Plc


class PlcRepository(ABC):
    @abstractmethod
    def get_plc_by_id(id: PlcId) -> Plc:
        ...

    @abstractmethod
    def get_all_plcs() -> list[Plc]:
        ...

    @abstractmethod
    def add_plc(plc: Plc):
        ...

    @abstractmethod
    def remove_plc(id: PlcId):
        ...

    @abstractmethod
    def get_all_sensors_from_plc_by_id(plc_id: PlcId) -> list[Sensor]:
        ...

    @abstractmethod
    def get_sensor_from_plc_by_id(plc_id: PlcId, sensor_id: SensorId) -> Sensor:
        ...

    @abstractmethod
    def add_sensor_with_plc(sensor: Sensor, plc_id: PlcId):
        ...

    @abstractmethod
    def remove_sensor_from_plc_by_id(plc_id: PlcId, sensor_id: SensorId):
        ...
