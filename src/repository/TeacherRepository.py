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

    def update(self, entity: TeacherModel) -> bool:
        try:
            self.logger.info("Updating teacher entity: %s", entity)

            with Session(engine) as session:
                existing_teacher = session.get(TeacherModel, entity.id)
                if existing_teacher is None:
                    self.logger.error("Teacher with ID %s not found", entity.id)
                    return False

                existing_teacher.user_id = entity.user_id
                existing_teacher.salary = entity.salary
                existing_teacher.specialization = entity.specialization

                session.commit()

            self.logger.info("Teacher entity updated successfully: %s", entity)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while updating the teacher: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while updating the teacher: %s", e)
            return False

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
                        "specialization": teacher.specialization,
                        "is_active": teacher.is_active,
                        "created_at": str(teacher.created_at),
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

    def delete(self, teacher_id: str) -> bool:
        try:
            self.logger.info("Soft deleting teacher with ID: %s", teacher_id)

            with Session(engine) as session:
                teacher_entity = session.get(TeacherModel, teacher_id)
                if not teacher_entity:
                    self.logger.warning("Teacher with ID %s not found for soft delete.", teacher_id)
                    return False

                teacher_entity.is_active = False
                session.commit()

            self.logger.info("Teacher with ID %s has been soft deleted.", teacher_id)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while soft deleting the teacher: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while soft deleting the teacher: %s", e)
            return False

