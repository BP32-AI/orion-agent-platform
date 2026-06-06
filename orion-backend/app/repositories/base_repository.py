# app/repositories/base_repository.py

from uuid import UUID

from sqlalchemy.orm import Session


class BaseRepository:

    def __init__(self, db: Session):
        self.db = db

    def get(self, model, obj_id: UUID):
        return (
            self.db.query(model)
            .filter(model.id == obj_id)
            .first()
        )

    def create(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj

    def delete(self, obj):
        self.db.delete(obj)
        self.db.commit()

        return True