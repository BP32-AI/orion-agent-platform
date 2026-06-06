# app/db/models/log.py

from sqlalchemy import Column, String, ForeignKey, Text

from app.db.session import Base
from app.db.models.base_model import BaseModel


class Log(Base, BaseModel):
    __tablename__ = "logs"

    workflow_run_id = Column(
        ForeignKey("workflow_runs.id"),
        nullable=True
    )

    level = Column(String, nullable=False)

    message = Column(Text, nullable=False)