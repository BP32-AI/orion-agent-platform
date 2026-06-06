# app/repositories/agent_repository.py

from uuid import UUID

from sqlalchemy.orm import Session

from app.db.models.agent import Agent
from app.repositories.base_repository import BaseRepository


class AgentRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create_agent(self, agent: Agent):
        return self.create(agent)

    def get_agent(self, agent_id: UUID):
        return (
            self.db.query(Agent)
            .filter(Agent.id == agent_id)
            .first()
        )

    def list_agents(self):
        return (
            self.db.query(Agent)
            .all()
        )

    def delete_agent(self, agent: Agent):
        return self.delete(agent)