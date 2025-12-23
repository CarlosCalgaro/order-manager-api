from fastapi import APIRouter
from order_manager_api.api.routes import orders
from order_manager_api.api.routes.pagseguro import orders as pagseguro_orders
api_router = APIRouter()
api_router.include_router(orders.router)
api_router.include_router(pagseguro_orders.router)