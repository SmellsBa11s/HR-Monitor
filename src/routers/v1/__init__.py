from fastapi import APIRouter
from routers.v1.user.user import router as user
from routers.v1.user.responses import router as user_request
from routers.v1.auth.auth import router as auth
from routers.v1.supervisor.admin import router as supervisor_admin


router = APIRouter(prefix="/v1")
router.include_router(auth, prefix="/user", tags=["Auth"])
router.include_router(user, prefix="/user", tags=["User"])
router.include_router(user_request, prefix="/response", tags=["User"])
router.include_router(supervisor_admin, prefix="/user", tags=["Supervisor"])
