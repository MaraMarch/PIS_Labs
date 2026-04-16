from dataclasses import dataclass, field
from datetime import datetime, timedelta
from uuid import uuid4
from .value_objects import IncidentStatus, Priority

@dataclass
class Incident:
    title: str
    description: str
    priority: Priority = Priority.LOW
    id: str = field(default_factory=lambda: str(uuid4()))
    status: IncidentStatus = IncidentStatus.NEW
    created_at: datetime = field(default_factory=datetime.utcnow)
    # Поле для дедлайна
    deadline: datetime = field(init=False)

    def __post_init__(self):
        # Бизнес-логика SLA: расчет дедлайна в зависимости от приоритета
        sla_hours = {
            Priority.LOW: 24,
            Priority.MEDIUM: 8,
            Priority.HIGH: 4,
            Priority.CRITICAL: 1
        }
        hours = sla_hours.get(self.priority, 24)
        self.deadline = self.created_at + timedelta(hours=hours)

    def resolve(self):
        self.status = IncidentStatus.RESOLVED
