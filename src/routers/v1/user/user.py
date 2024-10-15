from fastapi import APIRouter, Depends

from core import errors
from schemas.user import PasswordUpdate, GetMyInfo, GetMyStatistics, UpdateUserInfo

router = APIRouter()


@router.get("/me", response_model=GetMyInfo, responses=errors.with_errors())
async def get_my_info():
    """Get my personal information"""
    pass


@router.put(
    "/me/password",
    status_code=204,
    responses=errors.with_errors(
        errors.old_password_is_incorrect(), errors.password_is_too_weak()
    ),
)
async def change_my_password(data: PasswordUpdate):
    """Update password for my account"""
    pass


@router.get(
    "/me/responses", response_model=GetMyStatistics, responses=errors.with_errors()
)
async def get_my_response() -> GetMyStatistics:
    """Get my statistics"""
    pass


@router.put(
    "/info",
    status_code=204,
    responses=errors.with_errors(
        errors.access_denied(), errors.user_with_such_credentials_already_exists()
    ),
)
async def update_account_info():
    """Update account info by user of his account or update other user's info by supervisor"""
    pass
