from fastapi import APIRouter, Depends
from typing import List

from core import errors
from schemas.user import (
    RequestResponse,
    ProjectRequestBaseInfo,
    RequestsAllProjectRequest,
    CreateRequest,
    CheckRequest,
)


router = APIRouter()


@router.post(
    "/{student_id}/check/all",
    response_model=List[ProjectRequestBaseInfo],
    responses=errors.with_errors(),
)
async def check_requests(check_data: CheckRequest):
    pass


@router.post(
    "/{student_id}/check/",
    response_model=List[ProjectRequestBaseInfo],
    responses=errors.with_errors(),
)
async def check_request(application_id: int):
    pass


@router.post(
    "/{student_id}/send",
    response_model=List[ProjectRequestBaseInfo],
    responses=errors.with_errors(),
)
async def send_response():
    pass


@router.post(
    "/{student_id}/change",
    status_code=201,
    responses=errors.with_errors(
        errors.project_does_not_exists(), errors.invalid_route_parameters()
    ),
)
async def change_response():
    """Change response"""
    pass
