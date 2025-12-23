from typing import Generator
from order_manager_api.lib.pagseguro.order import PagseguroOrderRequest
from order_manager_api.models import Order, OrderItem

class PagSeguroOrderAdapter:

  def __init__(self, pagseguro_order_data: PagseguroOrderRequest):
      self.pagseguro_order_data = pagseguro_order_data

  def to_order(self) -> Order:
      order = Order(
          customer_name=self.pagseguro_order_data.customer.name,
          reference_id=self.pagseguro_order_data.reference_id,
          total_amount=0.0
      )
      order.items = list(self._generate_items())
      return order
  
  def _generate_items(self) -> Generator[OrderItem, None, None]:
      for item in self.pagseguro_order_data.items:
        yield OrderItem(
          name=item.name,
          quantity=item.quantity,
          price=item.unit_amount / 100.0,
          reference_id=item.reference_id
        )