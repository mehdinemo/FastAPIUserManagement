from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from app import (
    AuthRouter,
    UserRouter,
    User,
    CurrentActiveUser,
    create_db_and_tables
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(AuthRouter)
app.include_router(UserRouter)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(CurrentActiveUser)):
    return {"message": f"Hello {user.email}!"}
