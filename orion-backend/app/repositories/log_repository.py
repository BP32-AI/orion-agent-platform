# app/repositories/log_repository.py


from sqlalchemy.orm import Session

from app.db.models.log import Log
from app.repositories.base_repository import BaseRepository


class LogRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create_log(self, log: Log):
        return self.create(log)

    def get_run_logs(self, workflow_run_id):
        return (
            self.db.query(Log)
            .filter(
                Log.workflow_run_id == workflow_run_id
            )
            .all()
        )