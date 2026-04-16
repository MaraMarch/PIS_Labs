from sqlalchemy import select
from .models import IncidentTable
from src.domain.models import Incident

class PostgresIncidentRepository:
    def __init__(self, session):
        self.session = session

    async def save(self, incident: Incident):
        db_obj = IncidentTable(
            id=incident.id,
            title=incident.title,
            description=incident.description,
            priority=incident.priority.value,
            status=incident.status.value,
            created_at=incident.created_at,
            deadline=incident.deadline # Сохраняем дедлайн
        )
        self.session.add(db_obj)
        await self.session.commit()

    async def get_all(self):
        # Запрос всех записей из базы
        result = await self.session.execute(select(IncidentTable))
        return result.scalars().all()
