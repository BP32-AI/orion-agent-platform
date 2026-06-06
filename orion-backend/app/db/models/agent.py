# app/db/models/agent.py

from sqlalchemy import Column, String, Boolean, JSON

from app.db.session import Base
from app.db.models.base_model import BaseModel


class Agent(Base, BaseModel):
    __tablename__ = "agents"

    name = Column(String, nullable=False)

    role = Column(String, nullable=False)

    system_prompt = Column(String, nullable=False)

    model = Column(String, nullable=False)

    tools = Column(JSON, nullable=True)

    channels = Column(JSON, nullable=True)

    memory_enabled = Column(Boolean, default=True)

    is_active = Column(Boolean, default=True)