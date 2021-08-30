from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    password: str
    # my_products: List[Product] = []
    # my_sales: List[Order]
    # my_shopping: List[Order]


class Product(BaseModel):
    id: Optional[str] = None
    # user: User
    name: str
    details: str
    price: float
    available: bool = False
    # photo: Optional[str]

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[str] = None
    # user: User
    # product: Product
    amount: int
    delivery_place: bool = True
    observation: str
    # (entrega ou retirada)
    delivery_or_withdrawal: Optional[str] = 'Sem obeservações'
