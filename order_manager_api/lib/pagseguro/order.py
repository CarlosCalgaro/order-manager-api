from pydantic import BaseModel
from datetime import datetime

class Customer(BaseModel):
  name: str | None
  email: str | None
  tax_id: str | None

class Item(BaseModel):
  reference_id: str
  name: str
  quantity: int
  unit_amount: int

class PagseguroOrderRequest(BaseModel):
    id: str
    reference_id: str
    created_at: datetime
    customer: Customer
    items: list[Item]

      