import uuid

from domain.entities.plc import Plc
from domain.entities.sensor import Sensor
from domain.entities.temperature_sensor import TemperatureSensor
from domain.entities.temperature_source import TemperatureSource
from domain.value_objects.plc_id import PlcId
from domain.value_objects.sensor_id import SensorId
from domain.value_objects.temperature import Temperature


def test_should_add_sensor_to_plc() -> None:
    class TemperatureSource150(TemperatureSource):
        def get_current(self) -> Temperature:
            return Temperature(150)

    plc = Plc(PlcId(uuid.uuid4()))
    sensor = TemperatureSensor(SensorId(uuid.uuid4()), TemperatureSource150())

    plc.add_sensor(sensor)

    assert plc.get_sensors() == [sensor]


def test_should_read_from_sensor() -> None:
    class TemperatureSource150(TemperatureSource):
        def get_current(self) -> Temperature:
            return Temperature(150)

    plc = Plc(PlcId(uuid.uuid4()))
    sensor = TemperatureSensor(SensorId(uuid.uuid4()), TemperatureSource150())

    plc.add_sensor(sensor)

    assert plc.read_from_sensor(sensor.id).temperature == 150
