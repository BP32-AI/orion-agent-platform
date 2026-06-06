# app/services/agent_service.py

from uuid import UUID

from app.db.models.agent import Agent
from app.repositories.agent_repository import AgentRepository
from app.schemas.agent import AgentCreate, AgentUpdate


class AgentService:

    def __init__(self, repository: AgentRepository):
        self.repository = repository

    def create_agent(
        self,
        payload: AgentCreate
    ) -> Agent:

        agent = Agent(
            name=payload.name,
            role=payload.role,
            system_prompt=payload.system_prompt,
            model=payload.model,
            tools=payload.tools,
            channels=payload.channels,
            memory_enabled=payload.memory_enabled,
            is_active=payload.is_active,
        )

        return self.repository.create_agent(agent)

    def get_agent(
        self,
        agent_id: UUID
    ):
        return self.repository.get_agent(agent_id)

    def list_agents(self):
        return self.repository.list_agents()

    def delete_agent(
        self,
        agent_id: UUID
    ):
        agent = self.repository.get_agent(agent_id)

        if not agent:
            return False

        return self.repository.delete_agent(agent)

    def update_agent(
        self,
        agent_id: UUID,
        payload: AgentUpdate
    ):
        agent = self.repository.get_agent(agent_id)

        if not agent:
            return None

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(agent, key, value)

        self.repository.db.commit()
        self.repository.db.refresh(agent)

        return agent