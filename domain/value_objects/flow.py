
from dataclasses import dataclass
from domain.exceptions import FlowOutOfBoundsException


@dataclass(frozen=True)
class Flow:
    flow: float

    def __post_init__(self) -> FlowOutOfBoundsException:
        if self.flow < -100 or self.flow > 100:
            raise FlowOutOfBoundsException()
