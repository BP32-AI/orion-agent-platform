# app/repositories/execution_repository.py


from uuid import UUID

from sqlalchemy.orm import Session

from app.db.models.workflow_run import WorkflowRun
from app.repositories.base_repository import BaseRepository


class ExecutionRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create_run(self, workflow_run: WorkflowRun):
        return self.create(workflow_run)

    def get_run(self, run_id: UUID):
        return (
            self.db.query(WorkflowRun)
            .filter(WorkflowRun.id == run_id)
            .first()
        )

    def list_runs(self):
        return (
            self.db.query(WorkflowRun)
            .all()
        )