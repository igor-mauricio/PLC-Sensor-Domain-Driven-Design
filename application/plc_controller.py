from application.commands import (
    GetHomeCommand,
    ShowPlcsCommand,
    ShowPlcInfoCommand,
    ShowHelpCommand,
    ExitCommand,
    CreatePlcCommand,
    DeletePlcCommand,
    CreatePressureSensorCommand,
    CreateTemperatureSensorCommand,
    CreateFlowSensorCommand,
    ReadSensorCommand,
    DeleteSensorCommand,
)
from application.plc_service import PlcService
from application.presenter import Presenter
from domain.exceptions import DomainException, PlcNotFoundException


class PlcController:
    plc_service: PlcService
    presenter: Presenter
    running: bool = False

    def __init__(self, plc_service: PlcService, presenter: Presenter):
        self.plc_service = plc_service
        self.presenter = presenter

    def run(self) -> None:
        self.running = True
        self.get_home()
        while self.running:
            self.get_user_action()

    def get_home(self) -> None:
        self.presenter.home()

    def get_all_plcs(self) -> None:
        try:
            plcs = self.plc_service.get_all_plcs()
            self.presenter.show_plcs(plcs)
        except DomainException:
            self.presenter.show_error("Erro ao buscar CLPs")
        except Exception as e:
            print(e)

    def get_plc_info(self, plc_id: str) -> None:
        try:
            plc = self.plc_service.get_plc_info(plc_id)
            self.presenter.show_plc_info(plc)
        except DomainException:
            self.presenter.show_error("Erro ao buscar informações do CLP")

    def show_help(self) -> None:
        self.presenter.show_help()

    def exit(self) -> None:
        self.presenter.exit()
        self.running = False

    def create_plc(self) -> None:
        try:
            self.plc_service.create_plc()
            self.presenter.show_success("CLP Criado com sucesso")
        except DomainException:
            self.presenter.show_error("Erro ao criar CLP")

    def remove_plc(self, plc_id: str) -> None:
        try:
            self.plc_service.remove_plc(plc_id)
            self.presenter.show_success("CLP Removido com sucesso")
        except PlcNotFoundException:
            self.presenter.show_error("CLP não encontrado")
        except DomainException:
            self.presenter.show_error("Erro ao remover CLP")

    def add_temperature_sensor_to_plc(self, plc_id: str) -> None:
        try:
            self.plc_service.add_temperature_sensor_to_plc(plc_id)
            self.presenter.show_success("Sensor de Temperatura adicionado com sucesso")
        except DomainException:
            self.presenter.show_error("Erro ao adicionar sensor de temperatura")

    def add_pressure_sensor_to_plc(self, plc_id: str) -> None:
        try:
            self.plc_service.add_pressure_sensor_to_plc(plc_id)
            self.presenter.show_success("Sensor de Pressão adicionado com sucesso")
        except DomainException:
            self.presenter.show_error("Erro ao adicionar sensor de pressão")

    def add_flow_sensor_to_plc(self, plc_id: str) -> None:
        try:
            self.plc_service.add_flow_sensor_to_plc(plc_id)
            self.presenter.show_success("Sensor de Fluxo adicionado com sucesso")
        except DomainException:
            self.presenter.show_error("Erro ao adicionar sensor de fluxo")

    def read_from_sensor(self, plc_id: str, sensor_id: str) -> None:
        try:
            sensor = self.plc_service.get_sensor_from_plc(plc_id, sensor_id)
            self.presenter.show_success(f"Medição: {sensor.measure_string()}")

        except DomainException:
            self.presenter.show_error("Erro ao ler valor do sensor")

    def remove_sensor_from_plc(self, plc_id: str, sensor_id: str) -> None:
        try:
            self.plc_service.remove_sensor_from_plc(plc_id, sensor_id)
            self.presenter.show_success("Sensor removido com sucess")
        except DomainException:
            self.presenter.show_error("Erro ao remover sensor")
        except Exception as e:
            print(e)

    def get_user_action(self) -> None:
        action = self.presenter.get_user_action()

        if isinstance(action, GetHomeCommand):
            self.get_home()
        elif isinstance(action, ShowPlcsCommand):
            self.get_all_plcs()
        elif isinstance(action, ShowPlcInfoCommand):
            self.get_plc_info(action.plc_id)
        elif isinstance(action, ShowHelpCommand):
            self.show_help()
        elif isinstance(action, ExitCommand):
            self.exit()
        elif isinstance(action, CreatePlcCommand):
            self.create_plc()
        elif isinstance(action, DeletePlcCommand):
            self.remove_plc(action.plc_id)
        elif isinstance(action, CreatePressureSensorCommand):
            self.add_pressure_sensor_to_plc(action.plc_id)
        elif isinstance(action, CreateTemperatureSensorCommand):
            self.add_temperature_sensor_to_plc(action.plc_id)
        elif isinstance(action, CreateFlowSensorCommand):
            self.add_flow_sensor_to_plc(action.plc_id)
        elif isinstance(action, ReadSensorCommand):
            self.read_from_sensor(action.plc_id, action.sensor_id)
        elif isinstance(action, DeleteSensorCommand):
            self.remove_sensor_from_plc(action.plc_id, action.sensor_id)
        else:
            self.presenter.show_error("Comando inválido")
