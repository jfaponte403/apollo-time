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

    def find_all(self) -> Optional[List[CoursesModel]]:
        try:
            courses = []
            with Session(engine) as session:
                stmt = select(CoursesModel).where(CoursesModel.is_active == True)
                result = session.execute(stmt).scalars().all()

                for course in result:
                    courses.append(course)

            return courses if courses else None

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while fetching courses: %s", e)
            return None

        except Exception as e:
            self.logger.error("An unexpected error occurred while fetching courses: %s", e)
            return None

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