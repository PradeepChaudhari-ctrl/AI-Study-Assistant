from app.auth.jwt import create_access_token
from app.auth.repository import AuthRepository
from app.auth.security import hash_password, verify_password


class AuthService:
    def __init__(self, repository: AuthRepository):
        self.repository = repository

    async def register(self, full_name: str, email: str, password: str):
        existing_user = await self.repository.get_user_by_email(email)

        if existing_user:
            raise ValueError("Email already registered")

        hashed = hash_password(password)

        return await self.repository.create_user(
            full_name=full_name,
            email=email,
            hashed_password=hashed,
        )

    async def login(self, email: str, password: str):
        user = await self.repository.get_user_by_email(email)

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(password, user.hashed_password):
            raise ValueError("Invalid email or password")

        token = create_access_token({"sub": user.email})

        return {
            "access_token": token,
            "token_type": "bearer",
        }