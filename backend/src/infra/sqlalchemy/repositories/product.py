from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class ProductRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        create_product = models.Product(
            name=product.name,
            details=product.details,
            price=product.price,
            available=product.available
        )

        self.db.add(create_product)
        self.db.commit()
        self.db.refresh(create_product)
        return create_product

    def list_all(self):
        products = self.db.query(models.Product).all()
        return products

    def list_one(self):
        pass

    def delete(self):
        pass
