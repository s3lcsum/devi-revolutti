from fastapi import APIRouter

from routers import user

router = APIRouter()
router.include_router(user.router, tags=["user"], prefix="/hello")

