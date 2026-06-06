# app/services/workflow_service.py

from uuid import UUID

from app.db.models.workflow import Workflow
from app.repositories.workflow_repository import WorkflowRepository
from app.schemas.workflow import (
    WorkflowCreate,
    WorkflowUpdate,
)


class WorkflowService:

    def __init__(
        self,
        repository: WorkflowRepository
    ):
        self.repository = repository

    def create_workflow(
        self,
        payload: WorkflowCreate
    ):

        workflow = Workflow(
            name=payload.name,
            description=payload.description,
            graph_definition=payload.graph_definition,
            trigger_type=payload.trigger_type,
            is_active=payload.is_active,
        )

        return self.repository.create_workflow(
            workflow
        )

    def get_workflow(
        self,
        workflow_id: UUID
    ):
        return self.repository.get_workflow(
            workflow_id
        )

    def list_workflows(self):
        return self.repository.list_workflows()

    def update_workflow(
        self,
        workflow_id: UUID,
        payload: WorkflowUpdate
    ):

        workflow = self.repository.get_workflow(
            workflow_id
        )

        if not workflow:
            return None

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(workflow, key, value)

        self.repository.db.commit()
        self.repository.db.refresh(workflow)

        return workflow