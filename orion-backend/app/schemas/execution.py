# app/schemas/execution.py


from datetime import datetime
from uuid import UUID
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class WorkflowRunCreate(BaseModel):
    workflow_id: UUID

    input_payload: dict[str, Any] = Field(
        default_factory=dict
    )


class WorkflowRunResponse(BaseModel):
    id: UUID

    workflow_id: UUID

    status: str

    input_payload: dict[str, Any] = Field(
        default_factory=dict
    )

    output_payload: dict[str, Any] = Field(
        default_factory=dict
    )

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )