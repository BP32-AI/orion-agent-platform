# app/services/execution_service.py



from app.common.constants import (
    WORKFLOW_PENDING,
)

from app.db.models.workflow_run import WorkflowRun

from app.repositories.execution_repository import (
    ExecutionRepository,
)

from app.schemas.execution import (
    WorkflowRunCreate,
)


class ExecutionService:

    def __init__(
        self,
        repository: ExecutionRepository
    ):
        self.repository = repository

    def create_run(
        self,
        payload: WorkflowRunCreate
    ):

        workflow_run = WorkflowRun(
            workflow_id=payload.workflow_id,
            status=WORKFLOW_PENDING,
            input_payload=payload.input_payload,
        )

        return self.repository.create_run(
            workflow_run
        )

    def get_run(self, run_id):
        return self.repository.get_run(run_id)

    def list_runs(self):
        return self.repository.list_runs()