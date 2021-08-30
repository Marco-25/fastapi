from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class OrderRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, order: schemas.Order):
        create_order = models.Order(
            amount=order.amount,
            delivery_place=order.delivery_place,
            observation=order.observation,
            delivery_or_withdrawal=order.delivery_or_withdrawal
        )

        self.db.add(create_order)
        self.db.commit()
        self.db.refresh(create_order)
        return create_order

    def list_all(self):
        orders = self.db.query(models.Order).all()
        return orders

    def list_one(self):
        pass

    def delete(self):
        pass
