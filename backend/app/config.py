from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openai_api_key: str = ""
    anthropic_api_key: str = ""
    jwt_secret: str = "change-me"
    jwt_expire_minutes: int = 1440
    database_url: str = "sqlite:///./caregiver.db"
    chroma_persist_dir: str = "./chroma_data"

    chat_model: str = "claude-sonnet-5"
    embedding_model: str = "text-embedding-3-small"

    resend_api_key: str = ""
    email_from: str = "Caregiver Training Hub <onboarding@resend.dev>"
    frontend_url: str = "http://localhost:5173"
    password_reset_expire_minutes: int = 30


settings = Settings()
