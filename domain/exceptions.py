class DomainException(Exception): ...


class EmptyPlcIdException(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class EmptySensorIdException(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class FlowOutOfBoundsException(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class PressureOutOfBoundsException(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class SensorNotFound(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class TemperatureOutOfBoundsException(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class PlcNotFoundException(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class PlcWithIdAlreadyExists(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class SensorNotFoundException(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class SensorWithIdAlreadyExists(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)


class EmptyEntityIdException(DomainException):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(self.message)
