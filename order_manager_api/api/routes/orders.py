from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from order_manager_api.models import Order, OrderCreate, OrderPublic, OrderStatus
from order_manager_api.api.deps import SessionDep
from order_manager_api.api.routes.pagseguro.orders import router as pagseguro_orders
from sqlmodel import func, select

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", response_model=list[OrderPublic])
def list_orders(session: SessionDep, status: OrderStatus | None = None):
    query = select(Order).order_by(Order.created_at.asc())
    if status:
        query = query.where(Order.status == status)
    return session.exec(query).all()


class PrintOrdersRequest(BaseModel):
    ids: List[int]

@router.post("/print")
def mark_as_printed(session: SessionDep, print_order_request: PrintOrdersRequest):
    ids = print_order_request.ids
    # Fetch targeted orders
    orders = session.exec(select(Order).where(Order.id.in_(ids))).all()
    found_ids = {order.id for order in orders}

    # Update status to PRINTED
    for order in orders:
        order.sqlmodel_update({"status": OrderStatus.PRINTED})
        session.add(order)
    session.commit()
    
    return {
        "updated": len(orders),
        "not_found": [oid for oid in ids if oid not in found_ids],
    }
