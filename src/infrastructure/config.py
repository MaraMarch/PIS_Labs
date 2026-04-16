from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Значения по умолчанию, если нет в .env
    DATABASE_URL: str = "sqlite+asyncpg:///./test.db"
    GRPC_SERVER_HOST: str = "localhost"
    GRPC_SERVER_PORT: int = 50051

    class Config:
        env_file = ".env"

settings = Settings()
