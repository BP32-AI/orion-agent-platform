# app/schemas/workflow.py

from datetime import datetime
from uuid import UUID
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict


class WorkflowBase(BaseModel):
    name: str

    description: Optional[str] = None

    graph_definition: dict[str, Any]

    trigger_type: Optional[str] = None

    is_active: bool = True


class WorkflowCreate(WorkflowBase):
    pass


class WorkflowUpdate(BaseModel):
    name: Optional[str] = None

    description: Optional[str] = None

    graph_definition: Optional[dict[str, Any]] = None

    trigger_type: Optional[str] = None

    is_active: Optional[bool] = None


class WorkflowResponse(WorkflowBase):
    id: UUID

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )