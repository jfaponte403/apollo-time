import logging
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.database.database import engine
from src.models.LoginModel import LoginModel
from src.models.PostLoginModel import PostLoginModel

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class LoginRepository:
    @staticmethod
    def find_by_request(request: PostLoginModel) -> Optional[LoginModel]:
        try:
            username = str(request.username)
            password = str(request.password)
            logger.info("Searching for login for username: %s", username)

            with Session(engine) as session:
                stmt = select(LoginModel).where(
                    LoginModel.username == username,
                    LoginModel.password == password
                )

                login = session.execute(stmt).scalars().first()

                if login is None:
                    logger.warning("Login not found for username: %s", username)
                    return None

                logger.info("Login found for username: %s", username)
                return login

        except SQLAlchemyError as e:
            logger.error("Database error occurred: %s", e)
            return None

        except Exception as e:
            logger.error("An unexpected error occurred: %s", e)
            return None
