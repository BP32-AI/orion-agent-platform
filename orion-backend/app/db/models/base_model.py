# app/db/models/base_model.py

import uuid

from sqlalchemy.orm import declared_attr
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID


class BaseModel:
    @declared_attr
    def id(cls):
        return Column(
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4
        )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now()
    )