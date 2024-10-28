import logging
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from src.database.database import engine
from src.models.LoginModel import LoginModel
from src.repository.LoginRepository import LoginRepository
from src.repository.UserRepository import UserRepository
from src.schemas.TeacherModifySchema import TeacherModifySchema
from src.schemas.TeacherSchema import TeacherSchema
from src.models.TeachersModel import TeacherModel
from src.models.UserModel import UserModel
from src.repository.RoleRepository import RoleRepository
from src.repository.TeacherRepository import TeacherRepository

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

teacher = APIRouter()

@teacher.get("/", status_code=200, response_model=list)
def get_teachers():
    logger.info("Received request to fetch all teachers.")
    try:
        teachers = TeacherRepository().find_all()

        if teachers is None:
            logger.warning("No teachers found in the database.")
            raise HTTPException(status_code=404, detail="No teachers found.")

        logger.info(f"Fetched {len(teachers)} teachers from the database.")
        return teachers
    except Exception as e:
        logger.error(f"Error fetching teachers: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

@teacher.post("/", status_code=201, response_model=dict)
def post_teacher(request: TeacherSchema):
    logger.info("Received request to create a new teacher.")
    try:
        role_id = RoleRepository.get_teacher_id()
        logger.info(f"Retrieved role ID for teacher: {role_id}")

        if role_id is None:
            logger.warning("Teacher role ID not found.")
            raise HTTPException(status_code=404, detail="Teacher role not found.")

        user = UserModel.create_from_teacher_request(request=request, role_id=str(role_id))
        logger.info(f"Created user model for {request.username}")

        with Session(engine) as session:
            session.add(user)
            session.flush()

            login = LoginModel.create_from_teacher_request(request=request, user_id=str(user.id))
            session.add(login)

            teacher_entity = TeacherModel.create_from_request(request=request, user_id=str(user.id))
            session.add(teacher_entity)

            session.commit()

        logger.info(f"Successfully created teacher: {request.username}")
        return {
            "message": "Teacher created successfully.",
            "username": request.username,
            "password": request.password
        }

    except Exception as e:
        logger.error(f"Error creating teacher: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@teacher.delete("/{id}", status_code=200, response_model=dict)
def delete_teacher(id: str):
    logger.info(f"Received request to delete teacher with ID: {id}")

    try:
        teacher_entity = TeacherRepository().find_by_id(teacher_id=id)

        teacher_entity = UserRepository().delete_teacher_by_id(teacher_id=str(teacher_entity.user_id))

        if not teacher_entity:
            raise HTTPException(status_code=404, detail=f"Teacher with ID {id} not found")

        return {"message": "Teacher delete"}

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error deleting teacher with ID {id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@teacher.put("/{id}", status_code=200, response_model=dict)
def modify_teacher(id: str, request: TeacherModifySchema):
    logger.info(f"Received request to modify teacher with ID: {id}")

    try:
        teacher_repository = TeacherRepository()
        user_repository = UserRepository()
        login_repository = LoginRepository()

        teacher_entity = teacher_repository.find_by_id(teacher_id=id)
        if not teacher_entity:
            raise HTTPException(status_code=404, detail="Teacher not found")

        user_entity = user_repository.find_by_id(user_id=str(teacher_entity.user_id))
        if not user_entity:
            raise HTTPException(status_code=404, detail="User not found")

        login_entity = login_repository.find_by_user_id(user_id=str(teacher_entity.user_id))
        if not login_entity:
            raise HTTPException(status_code=404, detail="Login not found")

        if request.salary is not None:
            teacher_entity.salary = request.salary
        if request.specialization is not None:
            teacher_entity.specialization = request.specialization

        if request.name is not None:
            user_entity.name = request.name
        if request.email is not None:
            user_entity.email = request.email
        if request.phone_number is not None:
            user_entity.phone_number = request.phone_number

        if request.username is not None:
            login_entity.username = request.username
        if request.password is not None:
            login_entity.password = request.password

        teacher_repository.update(teacher_entity)
        user_repository.update(user_entity)
        login_repository.update(login_entity)

        logger.info(f"Teacher with ID {id} updated successfully.")
        return {"message": "Teacher updated successfully.", "id": id}

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error(f"Error modifying teacher with ID {id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


