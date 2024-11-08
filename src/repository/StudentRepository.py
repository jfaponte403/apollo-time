from typing import List, Optional, Type

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from sqlalchemy.testing.plugin.plugin_base import logging

from src.database.database import engine

import logging

from src.models.StudentsModel import StudentsModel
from src.models.UserModel import UserModel
from src.schemas.StudentModifySchema import StudentModifySchema


class StudentRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def find_by_id(self, student_id: str) -> Optional[StudentsModel]:
        self.logger.info(f"Fetching student with ID: {student_id}")
        try:
            with Session(engine) as session:
                student_entity = session.get(StudentsModel, student_id)
                if student_entity is None:
                    self.logger.warning(f"Student with ID {student_id} not found.")
                return student_entity
        except Exception as e:
            self.logger.error(f"Error fetching student with ID {student_id}: {str(e)}")
            raise e

    def update(self, student_data: StudentsModel) -> bool:
        try:
            self.logger.info("Updating student entity with ID: %s", student_data.id)

            with Session(engine) as session:
                student_entity = session.get(StudentsModel, student_data.id)
                if not student_entity:
                    self.logger.error("Student with ID %s not found for update.", student_data.id)
                    return False

                if student_data.degree_id is not None:
                    student_entity.degree_id = student_data.degree_id
                if student_data.gpa is not None:
                    student_entity.gpa = student_data.gpa

                session.commit()

            self.logger.info("Student entity updated successfully: %s", student_data.id)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while updating the student: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while updating the student: %s", e)
            return False

    def find_all(self) -> Optional[List[dict]]:
        try:
            students = []
            with Session(engine) as session:
                stmt = (
                    select(StudentsModel, UserModel)
                    .join(UserModel, StudentsModel.user_id == UserModel.id)
                )

                result = session.execute(stmt).all()

                for student, user in result:
                    students.append({
                        "student_id": student.id,
                        "user_id": user.id,
                        "user_name": user.name,
                        "email": user.email,
                        "phone_number": user.phone_number,
                        "degree_id": student.degree_id,
                        "gpa": student.gpa,
                        "is_active": student.is_active,
                        "created_at": student.created_at
                    })

            return students if students else None

        except Exception as e:
            self.logger.error("An error occurred while fetching students: %s", e)
            raise Exception(f"An error occurred while fetching students: {str(e)}")

    def delete(self, student_id: str) -> bool:
        try:
            self.logger.info("Soft deleting student with ID: %s", student_id)

            with Session(engine) as session:
                student_entity = session.get(StudentsModel, student_id)
                if not student_entity:
                    self.logger.warning("Student with ID %s not found for soft delete.", student_id)
                    return False

                student_entity.is_active = False
                session.commit()

            self.logger.info("Student with ID %s has been soft deleted.", student_id)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while soft deleting the student: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while soft deleting the student: %s", e)
            return False

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
