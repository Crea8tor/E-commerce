from enum import Enum
from pydantic import BaseModel
from decimal import Decimal


from schema.product import Product


class OrderStatus(Enum):
    completed = "COMPLETED"
    pending = "PENDING"
print(OrderStatus.completed.value)

stat = OrderStatus.completed.value

class Order(BaseModel):
    id: int
    customer_id: int
    items: list[int | Product]
    status: str = OrderStatus.pending.value

class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]

orders : list[Order]  = [
    Order(id=1, customer_id=1, items=[1,2])
]
