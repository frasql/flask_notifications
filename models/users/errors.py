class UserError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class UserNotFoundError(UserError):
    pass


class InvalidEmailError(UserError):
    pass


class UserAlreadyRegisteredError(UserError):
    pass

class IncorrectPasswordError(UserError):
    pass