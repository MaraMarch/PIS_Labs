from src.domain.models import Incident
from src.infrastructure.db.repository import PostgresIncidentRepository

class IncidentService:
    def __init__(self, repo: PostgresIncidentRepository, notification_client):
        self.repo = repo
        self.notification_client = notification_client

    async def report_incident(self, title: str, description: str, priority):
        # 1. Создаем доменный объект
        incident = Incident(title=title, description=description, priority=priority)

        # 2. Сохраняем в базу
        await self.repo.save(incident)

        # 3. Отправляем уведомление (gRPC)
        await self.notification_client.send_alert(incident)

        return incident
