class InfraException(Exception):
    ...


class InvalidCommandException(InfraException):
    def __init__(self, command: str):
        self.command = command
        self.message = f"Invalid command: {command}"
        super().__init__(self.message)


class InvalidArgumentCountException(InfraException):
    def __init__(self, expected: int, actual: int):
        self.expected = expected
        self.actual = actual
        self.message = f"Expected {expected} arguments, but got {actual}"
        super().__init__(self.message)
