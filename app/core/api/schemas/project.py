from uuid import UUID
from pydantic.main import BaseModel

from app.core.enums.project_status import ProjectStatus


class CreateInputProjectSchema(BaseModel):
    name: str
    status: ProjectStatus


class CreateOutputProjectSchema(BaseModel):
    id: UUID
    name: str
    status: ProjectStatus


class ReadOutputProjectSchema(BaseModel):
    id: UUID
    name: str
    status: ProjectStatus
