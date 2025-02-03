from uuid import UUID
from pydantic.main import BaseModel

from app.core.enums.project_status import ProjectStatus


class ProjectDTO(BaseModel):
    id: UUID
    name: str
    status: ProjectStatus
