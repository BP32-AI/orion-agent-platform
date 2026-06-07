# app/services/monitoring_service.py

from app.repositories.log_repository import (
    LogRepository,
)
class MonitoringService:

    def __init__(
        self,
        repository: LogRepository
    ):
        self.repository = repository

    def get_run_logs(
        self,
        workflow_run_id
    ):
        return self.repository.get_run_logs(
            workflow_run_id
        )