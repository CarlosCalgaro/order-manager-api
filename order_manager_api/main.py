from fastapi import FastAPI, APIRouter
from order_manager_api.api.main import api_router
from order_manager_api.core.db import engine, init_db
from sqlmodel import Session

with Session(engine) as session:
      init_db(session)

app = FastAPI()

router = APIRouter(prefix="/api", tags=["api"])

router.include_router(api_router)
app.include_router(router)