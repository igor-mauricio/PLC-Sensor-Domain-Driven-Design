from dataclasses import dataclass
from domain.exceptions import TemperatureOutOfBoundsException


@dataclass(frozen=True)
class Temperature:
    temperature: float

    def __post_init__(self) -> TemperatureOutOfBoundsException:
        if self.temperature <= -273.15:
            raise TemperatureOutOfBoundsException()
