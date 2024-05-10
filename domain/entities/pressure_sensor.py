from dataclasses import dataclass
from domain.value_objects.pressure import Pressure
from domain.value_objects.sensor_id import SensorId
from domain.entities.pressure_source import PressureSource
from domain.entities.sensor import Sensor


@dataclass
class PressureSensor(Sensor):
    id: SensorId
    source: PressureSource

    def measure(self) -> Pressure:
        return self.source.get_current()

    def measure_string(self) -> str:
        return f'{self.measure().pressure :.2f} Pa'
