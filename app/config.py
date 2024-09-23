from typing import Optional

from pydantic import computed_field, AnyUrl, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False, env_prefix="USER_MANAGEMENT_")

    db_name: str
    db_username: Optional[SecretStr] = None
    db_password: Optional[SecretStr] = None
    secret_key: SecretStr
    proxy: Optional[str] = Field(
        None,
        examples=["socks5://127.0.0.1:8080"],
        description="A proxy URL for GoogleOAuth2 authentication."
    )
    google_oauth_client_id: Optional[SecretStr] = None
    google_oauth_client_secret: Optional[SecretStr] = None
    google_oauth_redirect_url: Optional[AnyUrl] = Field(
        None,
        examples=["http://localhost:8501"],
        description="Optional arbitrary redirect URL for the GoogleOAuth2 flow."
    )

    @computed_field
    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_username.get_secret_value()}:{self.db_password.get_secret_value()}@localhost/{self.db_name}"


settings = Settings()
