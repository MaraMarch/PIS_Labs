from fastapi import APIRouter, Depends
from src.application.dto import IncidentCreateDTO
from src.application.services.incident_service import IncidentService
from src.api.dependencies import get_incident_service  # Эту функцию создадим сейчас

router = APIRouter()

@router.post("/incidents")
async def create_incident(
    data: IncidentCreateDTO,
    service: IncidentService = Depends(get_incident_service)
):
    incident = await service.report_incident(
        title=data.title,
        description=data.description,
        priority=data.priority
    )
    return {"id": incident.id, "status": "created"}
@router.get("/incidents")
async def list_incidents(service: IncidentService = Depends(get_incident_service)):
    # Мы просто берем данные из репозитория
    incidents = await service.repo.get_all()
    return incidents
