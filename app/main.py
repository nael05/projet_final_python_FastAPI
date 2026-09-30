from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import initialize_database
from app.routes import router
from app.security import initialize_default_user


@asynccontextmanager
async def lifespan(app: FastAPI):
	initialize_database()
	initialize_default_user()
	yield


app = FastAPI(title="API de médiathèque", lifespan=lifespan)
app.include_router(router)