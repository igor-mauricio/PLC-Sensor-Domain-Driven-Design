from application.plc_controller import PlcController
from application.plc_service import PlcService
from infra.flow_source_sine import FlowSourceSine
from infra.plc_repository_memory import PlcRepositoryMemory
from infra.presenter_terminal import PresenterTerminal
from infra.pressure_source_square_wave import PressureSourceSquareWave
from infra.temperature_source_random import TemperatureSourceRandom


def main() -> None:
    temperature_source = TemperatureSourceRandom(low=10, high=30)
    flow_source = FlowSourceSine(1, 5)
    pressure_source = PressureSourceSquareWave(0.2, 2)
    repository = PlcRepositoryMemory()
    presenter = PresenterTerminal()

    plc_service = PlcService(
        repository, temperature_source, flow_source, pressure_source
    )
    plc_controller = PlcController(plc_service, presenter)

    plc_controller.run()


if __name__ == "__main__":
    main()
