from fastapi.routing import APIRouter

from .project import router as project_router

router = APIRouter(prefix="/core")

router.include_router(project_router)
