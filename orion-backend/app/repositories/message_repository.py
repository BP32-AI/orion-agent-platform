# app/repositories/message_repository.py

from sqlalchemy.orm import Session

from app.db.models.message import Message
from app.repositories.base_repository import BaseRepository


class MessageRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create_message(self, message: Message):
        return self.create(message)

    def get_workflow_messages(self, workflow_run_id):
        return (
            self.db.query(Message)
            .filter(
                Message.workflow_run_id == workflow_run_id
            )
            .all()
        )