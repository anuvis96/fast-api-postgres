from functools import lru_cache

from pydantic import AnyUrl, BaseSettings, Field


class Settings(BaseSettings):
    DATABASE_DEV_URL: AnyUrl = Field(
        "postgres://postgres:postgres@prueba-api-db:5432/prueba-dev"
    )
    testing: int = Field(0)
    ENVIRONMENT: str = Field(...)
    WEB_APP_TITLE: str = Field(...)
    WEB_APP_DESCRIPTION: str = Field(...)
    WEB_APP_VERSION: str = Field(...)
    DEFAULT_EXPIRE_TIME: int = Field(3600)
    POSTGRES_DATABASE_URL: str = Field(...)

    DEFAULT_DATA: str = Field("False")


@lru_cache()
def get_settings() -> BaseSettings:
    return Settings()
