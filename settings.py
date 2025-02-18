from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Telegram
    TOKEN: str

    API_ID: str
    API_HASH: str
    PHONE: str
    PASSWORD: str | None

    # Redis
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
