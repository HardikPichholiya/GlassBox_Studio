"""Application configuration and settings

Load environment variables and expose typed settings. Expand as needed.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str | None = None  # e.g., postgres://...
    FIREBASE_PROJECT_ID: str | None = None
    ENV: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()


