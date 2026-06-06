# app/schemas/agent.py

from datetime import datetime
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AgentBase(BaseModel):
    name: str
    role: str
    system_prompt: str
    model: str

    tools: list[str] = Field(default_factory=list)
    channels: list[str] = Field(default_factory=list)

    memory_enabled: bool = True
    is_active: bool = True


class AgentCreate(AgentBase):
    pass


class AgentUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    system_prompt: Optional[str] = None
    model: Optional[str] = None

    tools: Optional[list[str]] = None
    channels: Optional[list[str]] = None

    memory_enabled: Optional[bool] = None
    is_active: Optional[bool] = None


class AgentResponse(AgentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )