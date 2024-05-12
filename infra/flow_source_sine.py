import math
from domain.value_objects.flow import Flow
from domain.entities.flow_source import FlowSource


class FlowSourceSine(FlowSource):
    _current = 0.0
    _step = 0.1
    _freq: float
    _amplitude: float

    def __init__(self, freq: float, amplitude: float):
        self._freq = freq
        self._amplitude = amplitude

    def get_current(self) -> Flow:
        flow = Flow(
            self._amplitude * math.sin(self._current * self._freq * 2 * math.pi)
        )
        self._current += self._step
        return flow
