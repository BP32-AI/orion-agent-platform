# app/db/models/workflow.py

from sqlalchemy import Column, String, JSON, Boolean

from app.db.session import Base
from app.db.models.base_model import BaseModel


class Workflow(Base, BaseModel):
    __tablename__ = "workflows"

    name = Column(String, nullable=False)

    description = Column(String, nullable=True)

    graph_definition = Column(JSON, nullable=False)

    trigger_type = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)