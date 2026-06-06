# app/repositories/memory_repository.py

from sqlalchemy.orm import Session

from app.db.models.memory import Memory
from app.repositories.base_repository import BaseRepository


class MemoryRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create_memory(self, memory: Memory):
        return self.create(memory)

    def list_agent_memories(self, agent_id):
        return (
            self.db.query(Memory)
            .filter(Memory.agent_id == agent_id)
            .all()
        )