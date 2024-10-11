from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from sqlalchemy.testing.plugin.plugin_base import logging

from src.database.database import engine

import logging

from src.models.StudentsModel import StudentsModel


class StudentRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)  # Ensure this is after logging is configured.

    def persist(self, entity: StudentsModel) -> bool:
        try:
            self.logger.info("Persisting degree entity: %s", entity)

            with Session(engine) as session:
                session.add(entity)
                session.commit()

            self.logger.info("Degree entity persisted successfully: %s", entity)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while persisting the degree: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while persisting the degree: %s", e)
            return False
