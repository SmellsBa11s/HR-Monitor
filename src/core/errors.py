from fastapi import HTTPException, status


def with_errors(*errors: HTTPException):
    errors_data = {}
    for err in errors:
        if err.status_code in errors_data:
            errors_data[err.status_code]["description"] += f"\n\n{err.detail}"
        else:
            errors_data[err.status_code] = {"description": err.detail}
    return errors_data


def invalid_credentials():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
    )


def token_validation_failed():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Failed token validation"
    )


def unauthorized():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization check failed"
    )


def token_expired():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
    )


def access_denied():
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")


def project_name_is_not_unique():
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Project name is already taken"
    )


def project_does_not_exists():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Project does not exist"
    )


def old_password_is_incorrect():
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Old password is incorrect!"
    )


def user_does_not_exist():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist!"
    )


def request_does_not_exist():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Request does not exist!"
    )


def user_with_such_credentials_already_exists():
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="User with such credentials already exists",
    )


def password_is_too_weak():
    return HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Password is too weak!"
    )


def invalid_route_parameters():
    return HTTPException(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        detail="Invalid route parameters",
    )


def bot_slug_not_unique():
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Bot slug is already taken"
    )
