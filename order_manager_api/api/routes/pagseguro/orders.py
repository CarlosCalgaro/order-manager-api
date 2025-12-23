from fastapi import APIRouter
from order_manager_api.models import Order, OrderCreate, OrderPublic
from order_manager_api.api.deps import SessionDep
from order_manager_api.lib.pagseguro.order import PagseguroOrderRequest
from order_manager_api.lib.adapters.pagseguro_order_adapter import PagSeguroOrderAdapter

router = APIRouter(prefix="/orders/pagseguro", tags=["pagseguro_orders"])


@router.post("/", response_model=OrderPublic)
def create_order(session: SessionDep, order_in: PagseguroOrderRequest):
    adapter = PagSeguroOrderAdapter(order_in)
    order = adapter.to_order()
    
    session.add(order)
    session.commit()
    session.refresh(order)
    return order