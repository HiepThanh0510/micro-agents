from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    LLM_URL: str = ""
    LLM_KEY: str = ""
    LLM_NAME: str = ""


settings = AppSettings()
