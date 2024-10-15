from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    surname: str
    name: str
    patronymic: Optional[str]
    position: Optional[str]
    phone: Optional[str]
    is_supervisor: Optional[bool]


class RequestAssign(BaseModel):
    user_id: int
    request_id: int


class SignUpHr(BaseModel):
    first_name: str
    last_name: str
    email: str
    # positon: Enum
    departament: str


class GetUserInfo(BaseModel):
    name: str
    surname: str
    patronymic: Optional[str]
    username: str
    email: EmailStr
    phone: Optional[str]
    telegram_id: Optional[str]
    is_active: bool
    is_supervisor: bool
    position: Optional[str]


class UpdateUserStatus(BaseModel):
    user_id: int
    is_supervisor: bool


class UpdateUserActivity(BaseModel):
    user_id: int
    is_active: bool
