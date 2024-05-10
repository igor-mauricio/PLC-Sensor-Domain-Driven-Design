
from domain.value_objects.plc_id import PlcId
from domain.value_objects.sensor_id import SensorId
from domain.entities.sensor import Sensor
from domain.exceptions import SensorNotFound


class Plc:
    _id: PlcId
    _sensors: list[Sensor]

    def __init__(self, id: PlcId):
        self._id = id
        self._sensors = []

    def read_from_sensor(self, sensorId: SensorId):
        for sensor in self._sensors:
            if sensor.get_id() == sensorId:
                return sensor.measure()
        raise SensorNotFound()

    def add_sensor(self, sensor: Sensor):
        self._sensors.append(sensor)

    def remove_sensor(self, sensor: Sensor):
        self._sensors.remove(sensor)

    def get_id(self) -> PlcId:
        return self._id

    def get_sensors(self) -> list[Sensor]:
        return self._sensors
