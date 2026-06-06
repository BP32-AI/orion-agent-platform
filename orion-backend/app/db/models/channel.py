# app/db/models/channel.py

from sqlalchemy import Column, String, Boolean

from app.db.session import Base
from app.db.models.base_model import BaseModel


class Channel(Base, BaseModel):
    __tablename__ = "channels"

    name = Column(String, nullable=False)

    type = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)