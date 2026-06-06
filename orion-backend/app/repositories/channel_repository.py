# app/repositories/channel_repository.py


from uuid import UUID

from sqlalchemy.orm import Session

from app.db.models.channel import Channel
from app.repositories.base_repository import BaseRepository


class ChannelRepository(BaseRepository):

    def __init__(
        self,
        db: Session
    ):
        super().__init__(db)

    def create_channel(
        self,
        channel: Channel
    ):
        return self.create(channel)

    def get_channel(
        self,
        channel_id: UUID
    ):
        return (
            self.db.query(Channel)
            .filter(Channel.id == channel_id)
            .first()
        )

    def list_channels(self):
        return (
            self.db.query(Channel)
            .all()
        )

    def delete_channel(
        self,
        channel: Channel
    ):
        return self.delete(channel)