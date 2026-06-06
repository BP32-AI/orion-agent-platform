# app/db/models/workflow_run.py

from sqlalchemy import Column, String, ForeignKey, JSON

from app.db.session import Base
from app.db.models.base_model import BaseModel


class WorkflowRun(Base, BaseModel):
    __tablename__ = "workflow_runs"

    workflow_id = Column(
        ForeignKey("workflows.id"),
        nullable=False
    )

    status = Column(String, nullable=False)

    input_payload = Column(JSON, nullable=True)

    output_payload = Column(JSON, nullable=True)