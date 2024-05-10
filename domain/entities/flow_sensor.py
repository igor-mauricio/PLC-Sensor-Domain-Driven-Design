from dataclasses import dataclass
from domain.value_objects.flow import Flow
from domain.value_objects.sensor_id import SensorId
from domain.entities.flow_source import FlowSource
from domain.entities.sensor import Sensor


@dataclass
class FlowSensor(Sensor):
    id: SensorId
    source: FlowSource

    def measure(self) -> Flow:
        return self.source.get_current()

    def measure_string(self) -> str:
        return f'{self.measure().flow:.2f} m³/s'
