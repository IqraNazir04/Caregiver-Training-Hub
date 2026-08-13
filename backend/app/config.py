from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openai_api_key: str = ""
    jwt_secret: str = "change-me"
    jwt_expire_minutes: int = 1440
    database_url: str = "sqlite:///./caregiver.db"
    chroma_persist_dir: str = "./chroma_data"

    chat_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"


settings = Settings()
