# app/schemas/common.py

from datetime import datetime
from uuid import UUID
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict


class TimestampMixin(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class APIResponse(BaseModel):
    success: bool = True
    message: str
    data: Optional[Any] = None


class HealthResponse(BaseModel):
    status: str