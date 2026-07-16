class AppError(Exception):
    """Base class for all custom application exceptions."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class NotFoundError(AppError):
    """Raised when a requested resource does not exist."""


class ConflictError(AppError):
    """Raised when an operation conflicts with the current state of a resource."""


class ValidationError(AppError):
    """Raised when input fails a business-logic validation rule."""

class UnauthorizedError(AppError):
    """Raised when authentication is missing or invalid."""


class ForbiddenError(AppError):
    """Raised when the authenticated principal lacks permission for the action."""