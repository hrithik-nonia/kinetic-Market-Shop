# built in module imports
from fastapi import status

# custom module imports


class AppException(Exception):
    """
    Base exception class — humare saare custom exceptions
    isी se inherit karenge. Isse ek common structure milta hai:
    message + status_code dono exception ke andar hi defined.
    """
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class UserAlreadyExistsException(AppException):
    """ happen when user signup with existing email in DB """
    def __init__(self, email: str):
        super().__init__(
            message=f"User with email '{email}' already exists",
            status_code=status.HTTP_409_CONFLICT,
        )


class InvalidCredentialsException(AppException):
    """ when login fails raise this exception """
    def __init__(self):
        super().__init__(
            message="Invalid email or password",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )