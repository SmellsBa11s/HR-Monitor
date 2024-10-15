from fastapi import APIRouter, Cookie, Depends, Response, Request

from core import errors
from schemas.auth import (
    LoginResponse,
    RefreshTokenResponse,
    LoginRequest,
    RefreshTokenRequest,
)

router = APIRouter()


@router.post("/login", response_model=LoginResponse, responses=errors.with_errors())
async def login(login_data: LoginRequest):
    pass


@router.post(
    "/refresh_token",
    response_model=RefreshTokenResponse,
    responses=errors.with_errors(),
)
async def refresh_token(refresh_data: RefreshTokenRequest):
    """Set new access token"""
    pass


@router.post("/logout", responses=errors.with_errors())
async def logout():
    """Delete user session and access token from cookie"""
    pass
