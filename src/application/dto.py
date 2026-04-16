from pydantic import BaseModel
from src.domain.value_objects import Priority

class IncidentCreateDTO(BaseModel):
    title: str
    description: str
    priority: Priority
