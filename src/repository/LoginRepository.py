import logging
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.database.database import engine
from src.models.LoginModel import LoginModel
from src.schemas.LoginSchema import LoginSchema

class LoginRepository:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def update(self, entity: LoginModel) -> bool:
        try:
            self.logger.info("Updating LoginModel entity: %s", entity)

            with Session(engine) as session:
                existing_login = session.get(LoginModel, entity.id)
                if existing_login is None:
                    self.logger.error("Login with ID %s not found", entity.id)
                    return False

                existing_login.user_id = entity.user_id
                existing_login.username = entity.username
                existing_login.password = entity.password

                session.commit()

            self.logger.info("LoginModel entity updated successfully: %s", entity)
            return True

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred while updating the login: %s", e)
            return False

        except Exception as e:
            self.logger.error("An unexpected error occurred while updating the login: %s", e)
            return False

    def find_by_user_id(self, user_id: str) -> Optional[LoginModel]:
        try:
            self.logger.info("Searching for login for user_id: %s", user_id)

            with Session(engine) as session:
                stmt = select(LoginModel).where(LoginModel.user_id == user_id)

                login = session.execute(stmt).scalars().first()

                if login is None:
                    self.logger.warning("Login not found for user_id: %s", user_id)
                    return None

                self.logger.info("Login found for user_id: %s", user_id)
                return login

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred: %s", e)
            return None

        except Exception as e:
            self.logger.error("An unexpected error occurred: %s", e)
            return None

    def find_by_request(self, request: LoginSchema) -> Optional[LoginModel]:
        try:
            username = str(request.username)
            password = str(request.password)
            self.logger.info("Searching for login for username: %s", username)

            with Session(engine) as session:
                stmt = select(LoginModel).where(
                    LoginModel.username == username,
                    LoginModel.password == password
                )

                login = session.execute(stmt).scalars().first()

                if login is None:
                    self.logger.warning("Login not found for username: %s", username)
                    return None

                self.logger.info("Login found for username: %s", username)
                return login

        except SQLAlchemyError as e:
            self.logger.error("Database error occurred: %s", e)
            return None

        except Exception as e:
            self.logger.error("An unexpected error occurred: %s", e)
            return None

    def persist(self, entity: LoginModel) -> bool:
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