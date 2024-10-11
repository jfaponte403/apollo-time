import logging
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import select

from typing import Optional, List

from sqlalchemy.testing.plugin.plugin_base import logging

from src.database.database import engine
from src.models.TeachersModel import TeacherModel
from src.models.UserModel import UserModel

import logging

class TeacherRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def find_all(self) -> Optional[List[dict]]:
        try:
            teachers = []
            with Session(engine) as session:
                stmt = (
                    select(TeacherModel, UserModel)
                    .join(UserModel, TeacherModel.user_id == UserModel.id)
                )

                result = session.execute(stmt).all()

                for teacher, user in result:
                    teachers.append({
                        "teacher_id": teacher.id,
                        "user_id": user.id,
                        "user_name": user.name,
                        "specialization": teacher.specialization
                    })

            return teachers if teachers else None

        except Exception as e:
            self.logger.error("An error occurred while fetching teachers: %s", e)
            raise Exception(f"An error occurred while fetching teachers: {str(e)}")

    def persist(self, entity: TeacherModel) -> bool:
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

    def find_by_id(self, teacher_id: str) -> Optional[TeacherModel]:
        try:
            with Session(engine) as session:
                stmt = select(TeacherModel).where(TeacherModel.id == str(teacher_id))
                teacher = session.execute(stmt).scalars().first()

                if teacher is None:
                    return None

                return teacher

        except Exception as e:
            self.logger.error("An unexpected error occurred while fetching the teacher: %s", e)
            raise e

