from abc import ABC
from dataclasses import dataclass


@dataclass
class UserCommand(ABC):
    ...


@dataclass
class GetHomeCommand(UserCommand):
    ...


@dataclass
class ShowPlcsCommand(UserCommand):
    ...


@dataclass
class ShowPlcInfoCommand(UserCommand):
    plc_id: str


@dataclass
class ShowHelpCommand(UserCommand):
    ...


@dataclass
class ExitCommand(UserCommand):
    ...


@dataclass
class CreatePlcCommand(UserCommand):
    ...


@dataclass
class DeletePlcCommand(UserCommand):
    plc_id: str


@dataclass
class CreatePressureSensorCommand(UserCommand):
    plc_id: str
    # sensor_id: str


@dataclass
class CreateFlowSensorCommand(UserCommand):
    plc_id: str
    # sensor_id: str


@dataclass
class CreateTemperatureSensorCommand(UserCommand):
    plc_id: str
    # sensor_id: str


@dataclass
class DeleteSensorCommand(UserCommand):
    plc_id: str
    sensor_id: str


@dataclass
class ReadSensorCommand(UserCommand):
    plc_id: str
    sensor_id: str
