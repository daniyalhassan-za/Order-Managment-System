from pydantic import BaseModel
from typing import List



class CustomerModel(BaseModel):
    name : str
    email : str
    phone: int | None = None

class ProductModel(BaseModel):
    product_id: int
    product_name : str
    quantity : float
    price : float

class PaymentModel(BaseModel):
    payment_method : str
    transaction_id : int
    Amount_paid : float


class OrderModel(BaseModel):
    customer : CustomerModel
    product : List[ProductModel]
    payment : PaymentModel




