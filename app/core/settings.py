import os
from typing import  Optional
from pydantic_settings import BaseSettings
from pydantic import model_validator


class Settings(BaseSettings):
    APPLICATION_NAME: str = "charts-be"
    ENV: str = "local"
 
 

    # Postgres DB
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[str] = ""


    @model_validator(mode="after")
    def generate_sqlalchemy_database_uri(self):
        if self.SQLALCHEMY_DATABASE_URI:
            return self

        self.SQLALCHEMY_DATABASE_URI = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return self


class LocalSettings(Settings):
    class Config:
        env_file = ".env"


class StagingSettings(Settings):
    class Config:
        env_file = ".env"
        extra = "ignore"


def get_settings() -> Settings:
    env = os.getenv("ENV", "local")
    print("environment ", env)
    if env.lower() == "local":
        return LocalSettings()
    elif env.lower() == "staging":
        env_copy = os.environ.copy()
        with open(".env", "w", encoding="utf-8") as f:
            for key, value in env_copy.items():
                f.write(f"{key}={value}\n")
        return StagingSettings()
    else:
        raise ValueError(f"Invalid environment: {env}")


settings: Settings = get_settings()
