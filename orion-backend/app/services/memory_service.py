# app/services/memory_service.py


from app.db.models.memory import Memory

from app.repositories.memory_repository import (
    MemoryRepository,
)

from app.schemas.memory import (
    MemoryCreate,
)


class MemoryService:

    def __init__(
        self,
        repository: MemoryRepository
    ):
        self.repository = repository

    def create_memory(
        self,
        payload: MemoryCreate
    ):

        memory = Memory(
            agent_id=payload.agent_id,
            memory_key=payload.memory_key,
            memory_value=payload.memory_value,
        )

        return self.repository.create_memory(
            memory
        )

    def get_agent_memories(
        self,
        agent_id
    ):
        return self.repository.list_agent_memories(
            agent_id
        )