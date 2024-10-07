import logging
from src.database.Base import Base
from src.database.database import engine
from src.models.AdminsModel import AdminsModel
from src.models.ClassroomsModel import ClassroomsModel
from src.models.CoursesModel import CoursesModel
from src.models.DegreeModel import DegreeModel
from src.models.LoginModel import LoginModel
from src.models.RoleModel import RoleModel
from src.models.SchedulesModel import SchedulesModel
from src.models.StudentsModel import StudentsModel
from src.models.SubjectsModel import SubjectsModel
from src.models.TeachersModel import TeacherModel
from src.models.UserModel import UserModel

logger = logging.getLogger(__name__)

def create_tables():
    try:
        logger.info("Starting table creation process...")

        Base.metadata.create_all(engine)

        logger.info("Tables created successfully.")

    except Exception as e:
        logger.error("An error occurred during table creation: %s", e)
        raise


if __name__ == "__main__":
    create_tables()
