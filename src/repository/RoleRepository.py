import logging
from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.database.database import engine
from src.models.RoleModel import RoleModel
from src.models.UserModel import UserModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class RoleRepository:

    @staticmethod
    def find_role_by_user_id(user_id: str) -> Optional[RoleModel]:
        try:
            logger.info("Searching for role associated with user id: %s", user_id)

            with Session(engine) as session:
                stmt = (
                    select(RoleModel)
                    .join(UserModel, RoleModel.id == UserModel.role_id)
                    .where(UserModel.id == user_id)
                )

                role = session.execute(stmt).scalars().first()

                if role is None:
                    logger.warning("Role not found for user id: %s", user_id)
                    return None

                logger.info("Role found for user id: %s", user_id)
                return role

        except SQLAlchemyError as e:
            logger.error("Database error occurred: %s", e)
        except Exception as e:
            logger.error("An unexpected error occurred: %s", e)
        return None
