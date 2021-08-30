from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id", name='fk_user_id'))
    user = relationship("User", back_populates="products")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    password = Column(String)
    products = relationship("Product", back_populates="user")


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    delivery_place = Column(Boolean)
    observation = Column(String)
    delivery_or_withdrawal = Column(String)  # (entrega ou retirada)
