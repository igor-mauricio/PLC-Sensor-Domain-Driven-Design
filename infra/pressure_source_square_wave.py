import math
from domain.entities.pressure_source import PressureSource
from domain.value_objects.flow import Flow
from domain.value_objects.pressure import Pressure


class PressureSourceSquareWave(PressureSource):
    _current: float = 0
    _period: float
    _gain: float
    _step: float = 0.1

    def __init__(self, period: float, gain: float):
        self._period = period
        self._gain = gain

    def get_current(self) -> Pressure:
        flow = Pressure((math.floor(self._current / self._period) %
                         2) * self._gain)
        self._current += self._step
        return flow
