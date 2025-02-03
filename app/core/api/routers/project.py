from typing import Annotated
from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import Response
from fastapi.param_functions import Body
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.core.api.schemas.project import CreateInputProjectSchema, CreateOutputProjectSchema, ReadOutputProjectSchema
from app.core.application.services.project import add_project, drop_project, fetch_project, fetch_project_list

router = APIRouter(tags=["Projects"])


@router.get("/projects")
@inject
async def get_projects(session: FromDishka[AsyncSession]) -> list[ReadOutputProjectSchema]:
    projects = await fetch_project_list(session)
    return [ReadOutputProjectSchema(id=project.id, name=project.name, status=project.status) for project in projects]


@router.get("/project")
@inject
async def get_project(project_id: UUID, session: FromDishka[AsyncSession]) -> ReadOutputProjectSchema:
    project = await fetch_project(project_id, session)
    return ReadOutputProjectSchema(id=project.id, name=project.name, status=project.status)


@router.delete("/project", response_class=Response, status_code=204)
@inject
async def delete_project(project_id: UUID, session: FromDishka[AsyncSession]) -> Response:
    await drop_project(project_id, session)
    return Response()


@router.post("/projects")
@inject
async def create_project(
    project_data: Annotated[
        CreateInputProjectSchema,
        Body(
            openapi_examples={
                "active": {
                    "summary": "Active Project",
                    "descriprion": 'Create project with status "Active"',
                    "value": {
                        "name": "112",
                        "status": "ACTIVE",
                    },
                },
                "on_technical_meintenance": {
                    "summary": "On Technical Meintenance Project",
                    "descriprion": 'Create project with status "On Technical Menteinance"',
                    "value": {
                        "name": "Active Sitizen",
                        "status": "ON_TECHNICAL_MAINTENANCE",
                    },
                },
            },
        ),
    ],
    session: FromDishka[AsyncSession],
) -> CreateOutputProjectSchema:
    project = await add_project(project_data, session)
    return CreateOutputProjectSchema(id=project.id, name=project.name, status=project.status)
