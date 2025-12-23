from typing import List
from decimal import Decimal
from datetime import datetime
from order_manager_api.lib.date_helper import DateHelper
from sqlmodel import Field, Relationship, SQLModel
from enum import Enum

class OrderStatus(str, Enum):
    PENDING="pending"
    PRINTED="printed"

class BaseOrderItem(SQLModel):
  reference_id: str
  name: str
  quantity: int
  price: Decimal = Field(default=0, max_digits=5, decimal_places=3)

class OrderItem(BaseOrderItem, table=True):
    __tablename__ : str = "order_items"

    id: int = Field(default=None, primary_key=True)
    order_id: int = Field(default=None, foreign_key="orders.id")
    order: "Order" = Relationship(back_populates="items")
    created_at: datetime = Field(
        default_factory=DateHelper.utcnow,  
        nullable=False
    )

class BaseOrder(SQLModel):
    customer_name: str
    reference_id: str
    total_amount: Decimal = Field(default=0, max_digits=10, decimal_places=2)

class Order(BaseOrder, table=True):
    __tablename__ : str = "orders"
    
    id: int = Field(default=None, primary_key=True)
    items : List["OrderItem"] = Relationship(back_populates="order")
    status: OrderStatus = Field(default=OrderStatus.PENDING) # Define um padrão
    created_at: datetime = Field(
        default_factory=DateHelper.utcnow,
        nullable=False
    )

class OrderCreate(BaseOrder):
    pass

class OrderPublic(BaseOrder):
    id: int
    status: OrderStatus
    items: List[OrderItem]
    created_at: datetime

class UserBase(SQLModel):
    name: str
    email: str
  
class User(SQLModel, table=True):
    __tablename__ : str = "users"

    id: int = Field(default=None, primary_key=True)
    token: str
    created_at: datetime = Field(
        default_factory=DateHelper.utcnow,
        nullable=False
    )

class UserPublic(UserBase):
    id: int