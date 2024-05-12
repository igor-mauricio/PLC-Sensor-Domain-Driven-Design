from abc import ABC, abstractmethod

from domain.entities.sensor import Sensor
from domain.value_objects.plc_id import PlcId
from domain.value_objects.sensor_id import SensorId
from domain.entities.plc import Plc


class PlcRepository(ABC):
    @abstractmethod
    def get_plc_by_id(self, id: PlcId) -> Plc: ...

    @abstractmethod
    def get_all_plcs(
        self,
    ) -> list[Plc]: ...

    @abstractmethod
    def add_plc(self, plc: Plc): ...

    @abstractmethod
    def remove_plc(self, id: PlcId): ...

    @abstractmethod
    def get_all_sensors_from_plc_by_id(self, plc_id: PlcId) -> list[Sensor]: ...

    @abstractmethod
    def get_sensor_from_plc_by_id(
        self, plc_id: PlcId, sensor_id: SensorId
    ) -> Sensor: ...

    @abstractmethod
    def add_sensor_with_plc(self, sensor: Sensor, plc_id: PlcId): ...

    @abstractmethod
    def remove_sensor_from_plc_by_id(self, plc_id: PlcId, sensor_id: SensorId): ...
