from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.auth.repository import AuthRepository
from app.auth.schemas import (
    Token,
    UserRegister,
    UserResponse,
)
from app.auth.service import AuthService
from app.database.models.user import User
from app.database.session import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register", response_model=UserResponse)
async def register(
    user: UserRegister,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(AuthRepository(db))

    try:
        created_user = await service.register(
            full_name=user.full_name,
            email=user.email,
            password=user.password,
        )

        return created_user

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(AuthRepository(db))

    try:
        return await service.login(
            email=form_data.username,
            password=form_data.password,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user