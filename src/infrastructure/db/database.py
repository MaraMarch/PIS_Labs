from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.infrastructure.config import settings

# Используем URL из конфига
engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

# Эта функция выдает сессию для каждого запроса
async def get_db():
    async with async_session() as session:
        yield session
