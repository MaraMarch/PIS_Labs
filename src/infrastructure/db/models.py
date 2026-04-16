from sqlalchemy import Column, String, Integer, DateTime
from src.infrastructure.db.database import Base

class IncidentTable(Base):
    __tablename__ = "incidents"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    priority = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime)
    deadline = Column(DateTime) # Новая колонка!
