import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    central configuration class.
    All environment variables are read here.
    Every other file import from this class.
    Never use os.getenv() anywhere else.
    """

    # App
    APP_NAME: str = os.getenv("APP_NAME", "Expense Tracker API")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    APP_ENV: str = os.getenv("APP_ENV", "development")

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    # JWT
    SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    def validate(self):
        """
        Call this on startup.
        Crashes immediately if required variables are missing.
        Better to crash at startup than fail silently in production.
        """
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL environment variable is required")
        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY environment variable is required")
        if len(self.SECRET_KEY) < 32:
            raise ValueError("SECRET_KEY must be at least 32 characters long")

settings = Settings()