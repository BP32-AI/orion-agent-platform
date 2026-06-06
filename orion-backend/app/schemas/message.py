# app/schemas/message.py

from datetime import datetime
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MessageResponse(BaseModel):
    id: UUID

    sender_agent_id: Optional[UUID] = None
    receiver_agent_id: Optional[UUID] = None

    workflow_run_id: Optional[UUID] = None

    content: str

    message_type: str

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )