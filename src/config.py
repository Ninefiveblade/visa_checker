from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Main project settings class

    Args:
        url: required field, visa url
            sample:
                - https://italy-vms.ru/autoform/...
    """

    url: str = Field(validation_alias=AliasChoices("url", "visa_url"))
    chat_id: str
    telegram_token: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
