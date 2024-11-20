import logging
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select

from src.database.database import engine
from src.models.CoursesModel import CoursesModel


class CourseRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def find_by_id(self, course_id: str) -> CoursesModel:
        try:
            self.logger.info("searching course")
            with Session(engine) as session:
                stmt = select(CoursesModel).where(CoursesModel.id == str(course_id))
                result = session.execute(stmt).scalars().first()
                return result
        except Exception as e:
            raise e

    def find_all(self) -> Optional[List[dict]]:
        try:
            courses = []
            with Session(engine) as session:
                stmt = select(CoursesModel)
                result = session.execute(stmt).scalars().all()

                for course in result:
                    courses.append(course.to_http_response())

            return courses

        except Exception as e:
            self.logger.error("An unexpected error occurred while retrieving degrees: %s", e)
            raise e

    def persist(self, course: CoursesModel) -> bool:
        try:
            with Session(engine) as session:
                session.add(course)
                session.commit()
                return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while persisting the degree: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while persisting the degree: %s", e)
            return False

    def delete(self, course_id: str) -> bool:
        try:
            self.logger.info("Soft deleting course with ID: %s", course_id)

            with Session(engine) as session:
                course_entity = session.get(CoursesModel, course_id)

                if not course_entity:
                    self.logger.warning("course with ID %s not found for soft delete.", course_id)
                    return False

                course_entity.is_active = False
                session.commit()

            self.logger.info("course with ID %s has been soft deleted.", course_id)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while soft deleting the degree: %s", e)
            raise e
        except Exception as e:
            self.logger.error("An unexpected error occurred while soft deleting the degree: %s", e)
            raise e

    def update(self, course: CoursesModel) -> bool:
        try:
            self.logger.info("Updating course with ID: %s", course.id)

            with Session(engine) as session:
                existing_course = session.get(CoursesModel, course.id)

                if not existing_course:
                    self.logger.warning("Course with ID %s not found for update.", course.id)
                    return False

                if course.classroom_id is not None:
                    existing_course.classroom_id = course.classroom_id
                if course.subject_id is not None:
                    existing_course.subject_id = course.subject_id
                if course.degrees_id is not None:
                    existing_course.degrees_id = course.degrees_id
                if course.teacher_id is not None:
                    existing_course.teacher_id = course.teacher_id
                if course.name is not None and course.name != "":
                    existing_course.name = course.name

                session.commit()
                self.logger.info("Course with ID %s has been successfully updated.", course.id)

            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while updating course with ID %s: %s", course.id, e)
            raise e

        except Exception as e:
            self.logger.error("An unexpected error occurred while updating course with ID %s: %s", course.id, e)
            raise e
