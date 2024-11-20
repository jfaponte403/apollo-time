import logging
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse

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

@teacher.get("/")
def get_teachers():
    logger.info("Received request to fetch all teachers.")
    try:
        teachers = TeacherRepository().find_all()

        if teachers is None:
            logger.warning("No teachers found in the database.")
            raise HTTPException(status_code=404, detail="No teachers found.")

        logger.info(f"Fetched {len(teachers)} teachers from the database.")
        return JSONResponse(
            status_code=200,
            content={"teachers": teachers}
        )
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

@teacher.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def delete_teacher(id: str):
    logger.info(f"Received request to delete teacher with ID: {id}")

    try:
        response = TeacherRepository().delete(str(id))

        if not response:
            logger.warning(f"Teacher with ID {id} not found or already inactive.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher with the specified ID does not exist or is already inactive."
            )

        logger.info(f"Teacher with ID {id} soft deleted successfully.")
        return

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

        if request.salary is not None and request.salary is not "":
            teacher_entity.salary = request.salary

        if request.specialization is not None and request.specialization is not "":
            teacher_entity.specialization = request.specialization

        if request.name is not None and request.name is not "":
            user_entity.name = request.name

        if request.email is not None and request.email is not "":
            user_entity.email = request.email

        if request.phone_number is not None and request.phone_number is not "":
            user_entity.phone_number = request.phone_number

        if request.username is not None and request.username is not "":
            login_entity.username = request.username

        if request.password is not None and request.password is not "":
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


