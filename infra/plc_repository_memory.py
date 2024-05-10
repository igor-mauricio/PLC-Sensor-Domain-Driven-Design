
from abc import ABC, abstractmethod

from domain.entities.sensor import Sensor
from domain.exceptions import PlcNotFoundException, PlcWithIdAlreadyExists, SensorNotFound
from domain.plc_repository import PlcRepository
from domain.value_objects.plc_id import PlcId
from domain.entities.plc import Plc
from domain.value_objects.sensor_id import SensorId


class PlcRepositoryMemory(PlcRepository):
    plcs: list[Plc]

    def __init__(self):
        self.plcs = []

    def get_plc_by_id(self, id: PlcId) -> Plc:
        for plc in self.plcs:
            if plc.get_id() == id:
                return plc
        raise PlcNotFoundException()

    def get_all_plcs(self) -> list[Plc]:
        return self.plcs

    def add_plc(self, plc: Plc):
        if any(plc.get_id() == p.get_id() for p in self.plcs):
            raise PlcWithIdAlreadyExists()

        self.plcs.append(plc)

    def remove_plc(self, id: PlcId):
        print(id)
        for i, plc in enumerate(self.plcs):
            if plc.get_id() == id:
                self.plcs.pop(i)
                return
        raise PlcNotFoundException()

    def get_all_sensors_from_plc_by_id(self, plc_id: PlcId) -> list[Sensor]:
        plc = self.get_plc_by_id(plc_id)

        return plc.get_sensors()

    def get_sensor_from_plc_by_id(self, plc_id: PlcId, sensor_id: SensorId) -> Sensor:
        sensors = self.get_all_sensors_from_plc_by_id(plc_id)
        for sensor in sensors:
            if sensor.id == sensor_id:
                return sensor
        raise SensorNotFound()

    def add_sensor_with_plc(self, sensor: Sensor, plc_id: PlcId):
        plc = self.get_plc_by_id(plc_id)
        plc.add_sensor(sensor)

    def remove_sensor_from_plc_by_id(self, plc_id: PlcId, sensor_id: SensorId):
        plc = self.get_plc_by_id(plc_id)
        for sensor in plc.get_sensors():
            if sensor.id == sensor_id:
                plc.remove_sensor(sensor)
                return
        raise SensorNotFound()
