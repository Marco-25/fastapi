from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.infra.sqlalchemy.repositories.user import UserRepository
from src.infra.sqlalchemy.repositories.order import OrderRepository
from src.infra.sqlalchemy.config.database import get_database, create_database
from src.schemas import schemas

# create_database()

app = FastAPI()


@app.get("/products", response_model=schemas.Product)
def list_products(db: Session = Depends(get_database)):
    return ProductRepository(db).list_all()


@app.post("/products", status_code=201, response_model=schemas.Product)
def create_product(product: schemas.Product, db: Session = Depends(get_database)):
    created_product = ProductRepository(db).create(product)
    return created_product


@app.get("/users")
def list_users(db: Session = Depends(get_database)):
    return UserRepository(db).list_all()


@app.post("/users", status_code=201)
def create_user(user: schemas.User, db: Session = Depends(get_database)):
    created_user = UserRepository(db).create(user)
    return created_user


@app.get("/orders")
def list_orders(db: Session = Depends(get_database)):
    return OrderRepository(db).list_all()


@app.post("/orders", status_code=201)
def create_orders(order: schemas.Order, db: Session = Depends(get_database)):
    created_order = OrderRepository(db).create(order)
    return created_order
