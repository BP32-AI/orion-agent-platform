# app/schemas/channel.py

# from datetime import datetime
# from uuid import UUID

# from pydantic import BaseModel, ConfigDict


# class ChannelResponse(BaseModel):
#     id: UUID

#     name: str
#     type: str

#     is_active: bool

#     created_at: datetime
#     updated_at: datetime

#     model_config = ConfigDict(
#         from_attributes=True
#     )


from datetime import datetime
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ChannelBase(BaseModel):
    name: str
    type: str
    is_active: bool = True


class ChannelCreate(ChannelBase):
    pass


class ChannelUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    is_active: Optional[bool] = None


class ChannelResponse(ChannelBase):
    id: UUID

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )