import logging
from typing import Optional, List

from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from src.database.database import engine
from src.models.ClassroomsModel import ClassroomsModel
from src.schemas.ClassroomSchema import ClassroomSchema


class ClassroomRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def delete(self, id: str):
        try:
            self.logger.info("deleting classrooms")
            with Session(engine) as session:
                stmt = update(ClassroomsModel).where(ClassroomsModel.id == id).values(
                    is_active=False
                )

                session.execute(stmt)
                session.commit()

                return

        except Exception as e:
            raise e

    def update(self, id: str, request: ClassroomSchema):
        try:
            self.logger.info("updating classrooms")
            with Session(engine) as session:
                stmt = update(ClassroomsModel).where(ClassroomsModel.id == id).values(
                    name=request.name,
                    type=request.type,
                    capacity=request.capacity
                )

                session.execute(stmt)
                session.commit()

                return

        except Exception as e:
            raise e

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
