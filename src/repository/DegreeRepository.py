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

    def delete(self, degree_id: str) -> bool:
        try:
            self.logger.info("Soft deleting degree with ID: %s", degree_id)

            with Session(engine) as session:
                degree_entity = session.get(DegreeModel, degree_id)

                if not degree_entity:
                    self.logger.warning("Degree with ID %s not found for soft delete.", degree_id)
                    return False

                degree_entity.is_active = False
                session.commit()

            self.logger.info("Degree with ID %s has been soft deleted.", degree_id)
            return True


        except Exception as e:
            self.logger.error("An unexpected error occurred while soft deleting the degree: %s", e)
            raise e

    def persist(self, degree_entity: DegreeModel) -> bool:
        try:
            self.logger.info("Persisting degree entity: %s", degree_entity)

            with Session(engine) as session:
                session.add(degree_entity)
                session.commit()

            self.logger.info("Degree entity persisted successfully: %s", degree_entity)
            return True
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
                    degrees.append(degree.to_http_response())

            return degrees

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while retrieving degrees: %s", e)
            return None

        except Exception as e:
            self.logger.error("An unexpected error occurred while retrieving degrees: %s", e)
            return None

    def find_by_id(self, degree_id: str) -> Optional[DegreeModel]:
        try:
            self.logger.info("Finding degree by ID: %s", degree_id)

            with Session(engine) as session:
                degree_entity = session.get(DegreeModel, degree_id)

                if degree_entity and degree_entity.is_active:
                    return degree_entity
                else:
                    self.logger.warning("Degree with ID %s not found or is inactive.", degree_id)
                    return None

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while finding the degree by ID: %s", e)
            return None

        except Exception as e:
            self.logger.error("An unexpected error occurred while finding the degree by ID: %s", e)
            return None

    def update(self, entity: DegreeModel) -> bool:
        try:
            self.logger.info("Updating degree entity: %s", entity)

            with Session(engine) as session:
                existing_degree = session.get(DegreeModel, entity.id)
                if existing_degree is None:
                    self.logger.error("Degree with ID %s not found", entity.id)
                    return False

                existing_degree.name = entity.name

                session.commit()

            self.logger.info("Degree entity updated successfully: %s", entity)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while updating the degree: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while updating the degree: %s", e)
            return False



