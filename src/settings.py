from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVER_ADDR: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    SERVER_TEST: bool = True

    JWT_SECRET: str
    JWT_ACCESS_EXPIRE: int
    JWT_REFRESH_EXPIRE: int

    ADMIN_USERNAME: str
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    MINIMAL_PASSWORD_LENGTH: int = 8


settings = Settings()
