from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.database import get_db
from src.infrastructure.db.repository import PostgresIncidentRepository
from src.infrastructure.grpc.client import NotificationClient
from src.application.services.incident_service import IncidentService

async def get_incident_service(db: AsyncSession = Depends(get_db)):
    repo = PostgresIncidentRepository(db)
    # Клиент gRPC пока создаем просто так, позже добавим настройки
    notification_client = NotificationClient()
    return IncidentService(repo, notification_client)
