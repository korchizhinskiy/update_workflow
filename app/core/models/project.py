from uuid import UUID

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from uuid6 import uuid7

from app.core.enums.project_status import ProjectStatus
from app.core.models.base import CoreBase


class Project(CoreBase):
    __tablename__: str = "core__project"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)

    name: Mapped[str] = mapped_column()
    status: Mapped[ProjectStatus] = mapped_column()
