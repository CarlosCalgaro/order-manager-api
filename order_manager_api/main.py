from fastapi import FastAPI
from order_manager_api.api.main import api_router
from order_manager_api.core.db import engine, init_db
from sqlmodel import Session



with Session(engine) as session:
      init_db(session)

app = FastAPI()
      
app.include_router(api_router)