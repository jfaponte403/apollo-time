import logging
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
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
