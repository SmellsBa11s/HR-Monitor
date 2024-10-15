from fastapi import APIRouter, Depends

from core import errors
from schemas.supervisor import (
    UserSignUp,
    UpdateUserActivity,
    UpdateUserStatus,
    GetUserInfo,
    SignUpHr,
)

router = APIRouter()


@router.post(
    "/sign_up",
    status_code=202,
    responses=errors.with_errors(errors.user_with_such_credentials_already_exists()),
)
async def sign_up_user(Sign_up_data: SignUpHr):
    """Register user on platform"""
    pass


@router.delete("/{user_id}", status_code=204, responses=errors.with_errors())
async def delete_user(user_id):
    """Delete user from platform"""
    pass


@router.put(
    "/supervisor_status/update",
    status_code=204,
    responses=errors.with_errors(errors.user_does_not_exist()),
)
async def supervisor_status_update():
    """Make user supervisor or downgrade to attendant"""
    pass


@router.get(
    "/{hr_staff_id}", response_model=GetUserInfo, responses=errors.with_errors()
)
async def get_hr_details():
    pass
