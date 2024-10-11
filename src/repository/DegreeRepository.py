import logging
from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.database.database import engine
from src.models.DegreeModel import DegreeModel
from src.models.LoginModel import LoginModel


class DegreeRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def persist(self, degree_entity: DegreeModel) -> bool:
        try:
            self.logger.info("Persisting degree entity: %s", degree_entity)

            with Session(engine) as session:
                session.add(degree_entity)
                session.commit()

            self.logger.info("Degree entity persisted successfully: %s", degree_entity)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while persisting the degree: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while persisting the degree: %s", e)
            return False

    def find_all(self) -> Optional[List[dict]]:
        try:
            degrees = []
            with Session(engine) as session:
                stmt = select(DegreeModel)
                result = session.execute(stmt).scalars().all()

                for degree in result:
                    degrees.append(degree.to_dict())

            return degrees

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while retrieving degrees: %s", e)
            return None

        except Exception as e:
            self.logger.error("An unexpected error occurred while retrieving degrees: %s", e)
            return None



