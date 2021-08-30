from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class UserRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: schemas.User):
        create_user = models.User(
            name=user.name,
            phone=user.phone,
            password=user.password
        )

        self.db.add(create_user)
        self.db.commit()
        self.db.refresh(create_user)
        return create_user

    def list_all(self):
        users = self.db.query(models.User).all()
        return users

    def list_one(self):
        pass

    def delete(self):
        pass
