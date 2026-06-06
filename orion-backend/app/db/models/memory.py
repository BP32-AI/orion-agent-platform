# app/db/models/memory.py

from sqlalchemy import Column, String, ForeignKey, Text

from app.db.session import Base
from app.db.models.base_model import BaseModel


class Memory(Base, BaseModel):
    __tablename__ = "memories"

    agent_id = Column(
        ForeignKey("agents.id"),
        nullable=False
    )

    memory_key = Column(String, nullable=False)

    memory_value = Column(Text, nullable=False)