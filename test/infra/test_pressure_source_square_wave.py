from infra.pressure_source_square_wave import PressureSourceSquareWave


def test_should_generate_square_wave() -> None:
    flow_source = PressureSourceSquareWave(0.2, 2)

    measurements = []
    for i in range(6):
        measurements.append(flow_source.get_current().pressure)
    assert measurements == [0, 0, 2, 2, 0, 0]
