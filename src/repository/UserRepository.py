import logging
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from src.database.database import engine
from src.models.TeachersModel import TeacherModel
from src.models.UserModel import UserModel

class UserRepository:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def persist(self, entity: UserModel) -> bool:
        try:
            self.logger.info("Persisting UserModel entity: %s", entity)

            with Session(engine) as session:
                session.add(entity)
                session.commit()

            self.logger.info("UserModel entity persisted successfully: %s", entity)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while persisting the degree: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while persisting the degree: %s", e)
            return False

    def delete_teacher_by_id(self, teacher_id: str) -> bool:
        try:
            with Session(engine) as session:
                self.logger.info("Deleting teacher with id: %s", teacher_id)
                user_entity = session.get(UserModel, teacher_id)

                if user_entity is None:
                    return False

                session.delete(user_entity)

                session.commit()

                return True

        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Database error occurred: {str(e)}")

        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
