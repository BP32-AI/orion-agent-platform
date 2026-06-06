# app/schemas/memory.py

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MemoryCreate(BaseModel):
    agent_id: UUID

    memory_key: str
    memory_value: str


class MemoryResponse(BaseModel):
    id: UUID

    agent_id: UUID

    memory_key: str
    memory_value: str

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )