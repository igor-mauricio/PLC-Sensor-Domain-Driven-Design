import uuid
from domain.entities.flow_sensor import FlowSensor
from domain.entities.flow_source import FlowSource
from domain.entities.plc import Plc
from domain.entities.pressure_sensor import PressureSensor
from domain.entities.pressure_source import PressureSource
from domain.entities.sensor import Sensor
from domain.entities.temperature_sensor import TemperatureSensor
from domain.entities.temperature_source import TemperatureSource
from domain.plc_repository import PlcRepository
from domain.value_objects.plc_id import PlcId
from domain.value_objects.sensor_id import SensorId


class PlcService:
    repository: PlcRepository

    temperature_source: TemperatureSource
    flow_source: FlowSource
    pressure_source: PressureSource

    def __init__(
        self,
        repository: PlcRepository,
        temperature_source: TemperatureSource,
        flow_source: FlowSource,
        pressure_source: PressureSource,
    ):
        self.repository = repository
        self.temperature_source = temperature_source
        self.flow_source = flow_source
        self.pressure_source = pressure_source

    def get_all_plcs(self) -> list[Plc]:
        return self.repository.get_all_plcs()

    def get_plc_info(self, plc_id: str):
        id = PlcId(uuid.UUID(plc_id))
        plc = self.repository.get_plc_by_id(id)
        return plc

    def create_plc(self):
        plc_id = PlcId(uuid.uuid4())
        plc = Plc(plc_id)
        self.repository.add_plc(plc)

    def remove_plc(self, plc_id: str):
        id = PlcId(uuid.UUID(plc_id))
        print(plc_id)
        self.repository.remove_plc(id)

    def add_temperature_sensor_to_plc(self, plc_id: str):
        id = PlcId(uuid.UUID(plc_id))
        sensor_id = SensorId(uuid.uuid4())
        sensor = TemperatureSensor(sensor_id, self.temperature_source)
        self.repository.add_sensor_with_plc(sensor, id)

    def add_pressure_sensor_to_plc(self, plc_id: str):
        id = PlcId(uuid.UUID(plc_id))
        sensor_id = SensorId(uuid.uuid4())
        sensor = PressureSensor(sensor_id, self.pressure_source)
        self.repository.add_sensor_with_plc(sensor, id)

    def add_flow_sensor_to_plc(self, plc_id: str):
        id = PlcId(uuid.UUID(plc_id))
        sensor_id = SensorId(uuid.uuid4())
        sensor = FlowSensor(sensor_id, self.flow_source)
        self.repository.add_sensor_with_plc(sensor, id)

    def remove_sensor_from_plc(self, plc_id: str, sensor_id: str):
        plc_id_object = PlcId(uuid.UUID(plc_id))
        sensor_id_object = SensorId(uuid.UUID(sensor_id))
        self.repository.remove_sensor_from_plc_by_id(plc_id_object, sensor_id_object)

    def read_from_sensor(self, plc_id: str, sensor_id: str):
        plc_id_object = PlcId(uuid.UUID(plc_id))
        sensor_id_object = SensorId(uuid.UUID(sensor_id))
        plc = self.repository.get_plc_by_id(plc_id_object)
        return plc.read_from_sensor(sensor_id_object)

    def get_sensor_from_plc(self, plc_id: str, sensor_id: str) -> Sensor:
        plc_id_object = PlcId(uuid.UUID(plc_id))
        sensor_id_object = SensorId(uuid.UUID(sensor_id))
        return self.repository.get_sensor_from_plc_by_id(
            plc_id_object, sensor_id_object
        )
