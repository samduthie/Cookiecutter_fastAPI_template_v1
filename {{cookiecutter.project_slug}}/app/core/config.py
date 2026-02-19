from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Application
    APP_NAME: str = "{{ cookiecutter.project_name }}"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "a_very_secret_key_that_should_be_changed"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # PostgreSQL
    POSTGRES_USER: str = "{{ cookiecutter.postgres_user }}"
    POSTGRES_PASSWORD: str = "{{ cookiecutter.postgres_password }}"
    POSTGRES_DB: str = "{{ cookiecutter.postgres_db }}"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    @property
    def database_uri_async(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Redis
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


settings = Settings()
