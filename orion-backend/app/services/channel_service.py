# app/services/channel_service.py

from uuid import UUID

from app.db.models.channel import Channel
from app.repositories.channel_repository import ChannelRepository
from app.schemas.channel import ChannelCreate, ChannelUpdate


class ChannelService:

    def __init__(
        self,
        repository: ChannelRepository
    ):
        self.repository = repository

    def create_channel(
        self,
        payload: ChannelCreate
    ):

        channel = Channel(
            name=payload.name,
            type=payload.type,
            is_active=payload.is_active,
        )

        return self.repository.create_channel(
            channel
        )

    def get_channel(
        self,
        channel_id: UUID
    ):
        return self.repository.get_channel(
            channel_id
        )

    def list_channels(self):
        return self.repository.list_channels()

    def update_channel(
        self,
        channel_id: UUID,
        payload: ChannelUpdate
    ):

        channel = self.repository.get_channel(
            channel_id
        )

        if not channel:
            return None

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(channel, key, value)

        self.repository.db.commit()
        self.repository.db.refresh(channel)

        return channel

    def delete_channel(
        self,
        channel_id: UUID
    ):

        channel = self.repository.get_channel(
            channel_id
        )

        if not channel:
            return False

        return self.repository.delete_channel(
            channel
        )