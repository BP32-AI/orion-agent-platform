# app/schemas/channel.py

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ChannelResponse(BaseModel):
    id: UUID

    name: str
    type: str

    is_active: bool

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )