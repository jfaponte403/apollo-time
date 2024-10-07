import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.database.database import engine
from src.models.DegreeModel import DegreeModel
from src.models.LoginModel import LoginModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class DegreeRepository:
    @staticmethod
    def persist(degree_entity: DegreeModel) -> bool:
        """
        Persist a DegreeModel instance to the database.

        Args:
            degree_entity (DegreeModel): The DegreeModel instance to be persisted.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        try:
            logger.info("Persisting degree entity: %s", degree_entity)

            with Session(engine) as session:
                session.add(degree_entity)
                session.commit()

            logger.info("Degree entity persisted successfully: %s", degree_entity)
            return True

        except SQLAlchemyError as e:
            logger.error("Database error occurred while persisting the degree: %s", e)
            return False

        except Exception as e:
            logger.error("An unexpected error occurred while persisting the degree: %s", e)
            return False
