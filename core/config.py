from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    DB_URL: str
    DB_ECHO: bool = True
    ADMIN_ID: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
