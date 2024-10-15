from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime

from schemas.enums import (
    EnumRequestStatus,
    EnumOrderByType,
    EnumRequestType,
    EnumStageType,
    EnumPositionType,
)


class PasswordUpdate(BaseModel):
    old_password: str
    new_password: str


class CheckRequest(BaseModel):
    stage: EnumStageType
    jobs_id: int
    per_page: int = 20
    page: int = 0
    order_by_creation: EnumOrderByType = EnumOrderByType.descending
    from_date: datetime
    to_date: datetime


class GetMyInfo(BaseModel):
    id: int
    name: str
    last_name: str
    patronymic: Optional[str]
    email: str
    # email: EmailStr
    position: EnumPositionType
    phone: Optional[str]
    is_active: bool
    department: str  # зависит от departmets_id


class GetMyStatistics(BaseModel):
    responses: int
    responses_is_open: int
    responses_is_studied: int
    responses_is_interview: int
    responses_is_interview_complete: int
    responses_is_technical_interview: int
    responses_is_technical_complete: int
    responses_is_offer: int
    average_is_open_request: int
    average_close_request: int


class UpdateUserInfo(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    position: Optional[str]


class RequestLogMessage(BaseModel):
    message_id: int
    user_id: int
    message_content: str
    created_at: datetime


class RequestResponse(BaseModel):
    status: EnumRequestStatus
    project_id: int
    requester_name: str
    request_type: EnumRequestType
    created_at: datetime
    attendant_id: Optional[int]
    request_text: str
    additional_data: Dict[str, Any]
    request_messages: List[RequestLogMessage]


class ProjectRequestBaseInfo(BaseModel):
    request_id: int
    status: EnumRequestStatus
    attendant_id: Optional[int]
    attendant_fullname: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    requester_name: str
    request_text: str


class RequestsAllProjectRequest(BaseModel):
    project_id: int
    user_id: Optional[int]
    limit: int = (20,)
    offset: int = 0
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    status: List[EnumRequestStatus]
    order_by_creation: EnumOrderByType = EnumOrderByType.descending


class RequestBody(BaseModel):
    text: str
    additional_data: Dict[Any, Any]


class CreateRequest(BaseModel):
    requester_name: str
    type: EnumRequestType
    content: RequestBody
