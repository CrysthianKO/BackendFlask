from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlmodel import create_engine


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    @property
    def database_url(self) -> str:
        return f"postgresql+psycopg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
engine = create_engine(settings.database_url, echo=True) # desativar echo para nao printar consultas