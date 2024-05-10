from dataclasses import dataclass
from domain.value_objects.sensor_id import SensorId
from domain.value_objects.temperature import Temperature
from domain.entities.sensor import Sensor
from domain.entities.temperature_source import TemperatureSource


@dataclass
class TemperatureSensor(Sensor):
    id: SensorId
    source: TemperatureSource

    def measure(self) -> Temperature:
        return self.source.get_current()

    def measure_string(self) -> str:
        return f'{self.measure().temperature:.2f} °C'
