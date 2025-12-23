from sqlmodel import Field, Session, SQLModel, create_engine, select
from .settings import Settings
from contextlib import contextmanager
from order_manager_api.models import User, Order, OrderItem  # importa os modelos para registrar os mappers


engine = create_engine(str(Settings.DATABASE_URI))

def init_db(session: Session):
    SQLModel.metadata.create_all(engine)
    