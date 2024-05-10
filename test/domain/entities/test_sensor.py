import uuid
from domain.entities.flow_sensor import FlowSensor
from domain.entities.flow_source import FlowSource
from domain.entities.pressure_sensor import PressureSensor
from domain.entities.pressure_source import PressureSource
from domain.entities.temperature_sensor import TemperatureSensor
from domain.entities.temperature_source import TemperatureSource
from domain.value_objects.flow import Flow
from domain.value_objects.pressure import Pressure
from domain.value_objects.sensor_id import SensorId
from domain.value_objects.temperature import Temperature


def test_temperature_sensor_should_sense_temperature():
    class TemperatureSource150(TemperatureSource):
        def get_current(self) -> Temperature:
            return Temperature(150)

    temperatureSource = TemperatureSource150()
    id = uuid.uuid4()
    sensorId = SensorId(id)
    temperatureSensor = TemperatureSensor(sensorId, temperatureSource)

    assert temperatureSensor.measure().temperature == 150


def test_pressure_sensor_should_sense_temperature():
    class PressureSource150(PressureSource):
        def get_current(self) -> Pressure:
            return Pressure(50)

    pressureSource = PressureSource150()
    id = uuid.uuid4()
    sensorId = SensorId(id)
    pressureSensor = PressureSensor(sensorId, pressureSource)

    assert pressureSensor.measure().pressure == 50


def test_flow_sensor_should_sense_flow():
    class FlowSource150(FlowSource):
        def get_current(self) -> Flow:
            return Flow(50)

    flowSource = FlowSource150()
    id = uuid.uuid4()
    sensorId = SensorId(id)
    flowSensor = FlowSensor(sensorId, flowSource)

    assert flowSensor.measure().flow == 50
