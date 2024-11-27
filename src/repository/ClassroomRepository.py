import logging
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from src.database.database import engine
from src.models.ClassroomsModel import ClassroomsModel


class ClassroomRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def find_all(self) -> Optional[List[ClassroomsModel]]:
        try:
            with Session(engine) as session:
                stmt = select(ClassroomsModel).where(ClassroomsModel.is_active == True)
                result = session.execute(stmt).scalars().all()
            return result if result else None

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while fetching classrooms: %s", e)
            return None

    def persist(self, classroom: ClassroomsModel) -> bool:
        try:
            with Session(engine) as session:
                session.add(classroom)
                session.commit()
                return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while persisting the classroom: %s", e)
            return False

    def update(self, classroom: ClassroomsModel) -> bool:
        try:
            self.logger.info("Updating classroom entity: %s", classroom)

            with Session(engine) as session:
                existing_classroom = session.get(ClassroomsModel, classroom.id)
                if existing_classroom is None:
                    self.logger.error("Classroom with ID %s not found", classroom.id)
                    return False

            
                existing_classroom.name = classroom.name
                existing_classroom.type = classroom.type
                existing_classroom.capacity = classroom.capacity
                existing_classroom.is_active = classroom.is_active  

                session.commit()

            self.logger.info("Classroom entity updated successfully: %s", classroom)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while updating the classroom: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while updating the classroom: %s", e)
            return False

    def delete(self, classroom_id: str) -> bool:
        try:
            self.logger.info("Soft deleting classroom with ID: %s", classroom_id)

            with Session(engine) as session:
                classroom_entity = session.get(ClassroomsModel, classroom_id)

                if not classroom_entity:
                    self.logger.warning("Classroom with ID %s not found for soft delete.", classroom_id)
                    return False

                classroom_entity.is_active = False  
                session.commit()

            self.logger.info("Classroom with ID %s has been soft deleted.", classroom_id)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while soft deleting the classroom: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while soft deleting the classroom: %s", e)
            return False
