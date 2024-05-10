from domain.entities.temperature_source import TemperatureSource
from domain.value_objects.temperature import Temperature


def test_temperature_source_should_generate_temperature():
    class TemperatureSource150(TemperatureSource):
        def get_current(self) -> Temperature:
            return Temperature(150)
    temperatureSource: TemperatureSource = TemperatureSource150()

    assert temperatureSource.get_current().temperature == 150
