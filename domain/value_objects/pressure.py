from dataclasses import dataclass
from domain.exceptions import PressureOutOfBoundsException


@dataclass(frozen=True)
class Pressure:
    pressure: float

    def __post_init__(self) -> PressureOutOfBoundsException:
        if self.pressure < -100 or self.pressure > 100:
            raise PressureOutOfBoundsException()
