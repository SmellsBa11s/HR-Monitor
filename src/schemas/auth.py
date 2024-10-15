from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    refresh: str


class RefreshTokenRequest(BaseModel):
    refresh: str


class RefreshTokenResponse(BaseModel):
    refresh: str
