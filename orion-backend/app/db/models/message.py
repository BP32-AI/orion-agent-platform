# app/db/models/message.py
from sqlalchemy import Column, String, ForeignKey, Text

from app.db.session import Base
from app.db.models.base_model import BaseModel


class Message(Base, BaseModel):
    __tablename__ = "messages"

    sender_agent_id = Column(
        ForeignKey("agents.id"),
        nullable=True
    )

    receiver_agent_id = Column(
        ForeignKey("agents.id"),
        nullable=True
    )

    workflow_run_id = Column(
        ForeignKey("workflow_runs.id"),
        nullable=True
    )

    content = Column(Text, nullable=False)

    message_type = Column(String, nullable=False)