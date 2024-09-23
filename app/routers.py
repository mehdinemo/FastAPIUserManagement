from fastapi import Depends, APIRouter

from .config import settings
from .schemas import UserCreate, UserRead, UserUpdate
from .users import (
    auth_backend,
    current_active_user,
    fastapi_users,
    google_oauth_client,
)

SECRET = settings.secret_key.get_secret_value()

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

auth_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
auth_router.include_router(fastapi_users.get_reset_password_router())
auth_router.include_router(fastapi_users.get_verify_router(UserRead))
auth_router.include_router(
    fastapi_users.get_oauth_router(
        google_oauth_client,
        auth_backend,
        SECRET,
        redirect_url=settings.google_oauth_redirect_url,
        is_verified_by_default=True
    ),
    prefix="/google"
)

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(current_active_user)],
    responses={404: {"description": "Not found"}},
)

user_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
