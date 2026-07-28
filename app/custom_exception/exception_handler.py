# built in module imports
from fastapi import Request
from fastapi.responses import JSONResponse


# custom modul imports
from app.custom_exception.custom_exceptions import AppException


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


def register_exception_handlers(app):
    app.add_exception_handler(AppException, app_exception_handler)