from domain.primitives.entity import Entity
from domain.value_objects.plc_id import PlcId
from domain.value_objects.sensor_id import SensorId
from domain.entities.sensor import Sensor
from domain.exceptions import SensorNotFound


class Plc(Entity):
    _sensors: list[Sensor]
    id: PlcId

    def __init__(self, id: PlcId):
        super().__init__(id)
        self._sensors = []

    def read_from_sensor(self, sensorId: SensorId):
        for sensor in self._sensors:
            if sensor.id == sensorId:
                return sensor.measure()
        raise SensorNotFound()

    def add_sensor(self, sensor: Sensor):
        self._sensors.append(sensor)

    def remove_sensor(self, sensor: Sensor):
        self._sensors.remove(sensor)

    def get_sensors(self) -> list[Sensor]:
        return self._sensors
