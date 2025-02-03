from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import delete, select

from app.core.api.schemas.project import CreateInputProjectSchema
from app.core.application.dto.project import ProjectDTO
from app.core.application.exceptions import ProjectNotFoundError
from app.core.models.project import Project


async def fetch_project(project_id: UUID, session: AsyncSession) -> ProjectDTO:
    query = select(Project).where(Project.id == project_id)
    project = await session.scalar(query)
    if not project:
        raise ProjectNotFoundError()
    return ProjectDTO(id=project.id, name=project.name, status=project.status)


async def fetch_project_list(session: AsyncSession) -> list[ProjectDTO]:
    query = select(Project)
    projects = await session.scalars(query)
    return [ProjectDTO(id=project.id, name=project.name, status=project.status) for project in projects]


async def drop_project(project_id: UUID, session: AsyncSession) -> None:
    query = select(Project).where(Project.id == project_id)
    project = await session.scalar(query)

    if not project:
        raise ProjectNotFoundError()

    stmt = delete(Project).where(Project.id == project_id)
    await session.execute(stmt)
    await session.commit()


async def add_project(project_data: CreateInputProjectSchema, session: AsyncSession) -> ProjectDTO:
    project = Project(
        name=project_data.name,
        status=project_data.status,
    )
    session.add(project)
    await session.commit()
    return ProjectDTO(id=project.id, name=project.name, status=project.status)
