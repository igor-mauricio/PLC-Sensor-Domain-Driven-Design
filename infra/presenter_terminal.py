from application.commands import *
from application.presenter import Presenter
from domain.entities.flow_sensor import FlowSensor
from domain.entities.plc import Plc
from domain.entities.pressure_sensor import PressureSensor
from domain.entities.temperature_sensor import TemperatureSensor
from infra.exceptions import *


class PresenterTerminal(Presenter):
    def home(self):
        print("Bem vindo ao sistema de controle de CLPs!")
        print("Digite 'help' para ver os comandos disponíveis")

    def show_plcs(self, plcs: list[Plc]):
        if len(plcs) == 0:
            self.show_info("Nenhum CLP disponível")
            return

        print("CLPs disponíveis:")
        for plc in plcs:
            print(f"- ID: {plc.id}")
            print(f"  Quantidade de Sensores: {len(plc.get_sensors())}")

    def show_plc_info(self, plc: Plc):
        print("Informações do CLP:")
        print(f"- ID: {plc.id}")
        sensors = plc.get_sensors()
        if len(sensors) == 0:
            print("- Nenhum sensor cadastrado")
            return
        print(f"- Sensores:")
        for sensor in sensors:
            print(f"-- ID: {sensor.id}")
            if isinstance(sensor, TemperatureSensor):
                print(f"   Tipo: Temperatura")
            elif isinstance(sensor, PressureSensor):
                print(f"   Tipo: Pressão")
            elif isinstance(sensor, FlowSensor):
                print(f"   Tipo: Fluxo")

    def show_help(self):
        print("Comandos disponíveis:")
        print("- list: Listar CLPs")
        print("- info <plc_id>: Exibir informações de um CLP")
        print("- create: Criar um CLP")
        print("- remove <plc_id>: Remover um CLP")
        print("- add_temp <plc_id>: Adicionar sensor de temperatura a um CLP")
        print("- add_pressure <plc_id>: Adicionar sensor de pressão a um CLP")
        print("- add_flow <plc_id>: Adicionar sensor de vazão a um CLP")
        print("- read <plc_id> <sensor_id>: Ler um sensor")
        print("- help: Exibir esta mensagem")
        print("- exit: Sair do sistema")

    def show_success(self, message):
        print("\x1b[6;30;42m" + message + "\x1b[0m")

    def show_error(self, message):
        print("\x1b[6;30;41m" + message + "\x1b[0m")

    def show_info(self, message):
        print("\x1b[6;30;44m" + message + "\x1b[0m")

    def exit(self):
        print("Encerrando sistema...")

    def get_user_action(self) -> UserCommand:
        while True:
            action = input("> ")
            try:
                user_command = self.parse_user_action(action)
                return user_command
            except InvalidCommandException as e:
                self.show_error(f"Comando inválido: {e.command}")
            except InvalidArgumentCountException as e:
                self.show_error(
                    f"Quantidade de argumentos inválida: {e.expected} esperados, {e.actual} recebidos"
                )

    def parse_user_action(self, action: str) -> UserCommand:
        action_parts = action.split(" ")
        command = action_parts[0]
        args = action_parts[1:]

        if command == "list":
            if len(args) != 0:
                raise InvalidArgumentCountException(0, len(args))
            return ShowPlcsCommand()
        elif command == "info":
            if len(args) != 1:
                raise InvalidArgumentCountException(1, len(args))
            return ShowPlcInfoCommand(args[0])
        elif command == "create":
            if len(args) != 0:
                raise InvalidArgumentCountException(0, len(args))
            return CreatePlcCommand()
        elif command == "remove":
            if len(args) != 1:
                raise InvalidArgumentCountException(1, len(args))
            return DeletePlcCommand(args[0])
        elif command == "add_temp":
            if len(args) != 1:
                raise InvalidArgumentCountException(2, len(args))
            return CreateTemperatureSensorCommand(args[0])
        elif command == "add_pressure":
            if len(args) != 1:
                raise InvalidArgumentCountException(2, len(args))
            return CreatePressureSensorCommand(args[0])
        elif command == "add_flow":
            if len(args) != 1:
                raise InvalidArgumentCountException(2, len(args))
            return CreateFlowSensorCommand(args[0])
        elif command == "help":
            if len(args) != 0:
                raise InvalidArgumentCountException(0, len(args))
            return ShowHelpCommand()
        elif command == "exit":
            if len(args) != 0:
                raise InvalidArgumentCountException(0, len(args))
            return ExitCommand()

        elif command == "read":
            if len(args) != 2:
                raise InvalidArgumentCountException(2, len(args))
            return ReadSensorCommand(args[0], args[1])

        raise InvalidCommandException(command)
