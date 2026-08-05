"""
Application configuration.

Loads all environment variables using Pydantic Settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    # API
    API_V1_PREFIX: str

    # CORS
    BACKEND_CORS_ORIGINS: str

    # Database
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()