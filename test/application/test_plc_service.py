import uuid

from application.plc_service import PlcService
from domain.entities.pressure_source import PressureSource
from domain.value_objects.pressure import Pressure
from infra.pressure_source_square_wave import PressureSourceSquareWave


# def test_pressure_sensor_should_sense_temperature():

#     pressureSource = PressureSourceSquareWave(0.2)
#     id = uuid.uuid4()
#     sensorId = SensorId(id)
#     pressureSensor = PressureSensor(sensorId, pressureSource)

#     assert pressureSensor.measure().pressure == 50
