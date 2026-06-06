# app/repositories/workflow_repository.py

from uuid import UUID

from sqlalchemy.orm import Session

from app.db.models.workflow import Workflow
from app.repositories.base_repository import BaseRepository


class WorkflowRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create_workflow(self, workflow: Workflow):
        return self.create(workflow)

    def get_workflow(self, workflow_id: UUID):
        return (
            self.db.query(Workflow)
            .filter(Workflow.id == workflow_id)
            .first()
        )

    def list_workflows(self):
        return (
            self.db.query(Workflow)
            .all()
        )