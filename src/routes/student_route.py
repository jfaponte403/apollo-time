from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
import logging

from src.database.database import engine
from src.models.LoginModel import LoginModel
from src.models.StudentsModel import StudentsModel
from src.models.UserModel import UserModel
from src.repository.LoginRepository import LoginRepository
from src.repository.RoleRepository import RoleRepository
from src.repository.StudentRepository import StudentRepository
from src.repository.UserRepository import UserRepository
from src.schemas.StudentModifySchema import StudentModifySchema
from src.schemas.StudentSchema import StudentSchema

logger = logging.getLogger(__name__)

student = APIRouter()


@student.put("/{id}", status_code=status.HTTP_200_OK, response_model=dict)
def update_student(id: str, request: StudentModifySchema):
    logger.info(f"Received request to update student with ID: {id}")

    student_repository = StudentRepository()
    user_repository = UserRepository()
    login_repository = LoginRepository()

    student_entity = student_repository.find_by_id(student_id=id)
    if not student_entity:
        logger.warning(f"Student with ID {id} not found for update.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    user_entity = user_repository.find_by_id(user_id=str(student_entity.user_id))
    if not user_entity:
        logger.warning(f"User associated with student ID {id} not found for update.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    login_entity = login_repository.find_by_user_id(user_id=str(student_entity.user_id))
    if not login_entity:
        logger.warning(f"Login associated with user ID {student_entity.user_id} not found for update.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Login not found")

    # Update student attributes if provided in the request
    if request.degree_id not in (None, ""):
        student_entity.degree_id = request.degree_id

    if request.gpa not in (None, ""):
        student_entity.gpa = request.gpa

    # Update user attributes if provided in the request
    if request.user_name not in (None, ""):
        user_entity.name = request.user_name
    if request.email not in (None, ""):
        user_entity.email = request.email
    if request.phone_number not in (None, ""):
        user_entity.phone_number = request.phone_number

    # Update login attributes if provided in the request
    if request.username not in (None, ""):
        login_entity.username = request.username
    if request.password not in (None, ""):
        login_entity.password = request.password

    # Perform updates
    if not student_repository.update(student_entity):
        logger.error(f"Failed to update student with ID {id}.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update student")

    if not user_repository.update(user_entity):
        logger.error(f"Failed to update user associated with student ID {id}.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update user")

    if not login_repository.update(login_entity):
        logger.error(f"Failed to update login associated with user ID {student_entity.user_id}.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update login")

    logger.info(f"Student with ID {id} and associated user and login updated successfully.")
    return {"message": "Student, user, and login updated successfully."}

@student.get("/", response_model=dict, status_code=status.HTTP_200_OK)
def get_students():
    logger.info("Received request to retrieve all students.")

    try:
        students = StudentRepository().find_all()

        if students is None:
            logger.warning("No students found.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No students found in the database."
            )

        logger.info(f"Successfully retrieved {len(students)} students.")
        return {"message": "Students retrieved successfully.", "students": students}

    except Exception as e:
        logger.error(f"Error retrieving students: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An unexpected error occurred: {str(e)}")

@student.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: str):
    logger.info(f"Received request to delete student with ID: {id}")

    try:
        response = StudentRepository().delete(str(id))

        if not response:
            logger.warning(f"Student with ID {id} not found or already inactive.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student with the specified ID does not exist or is already inactive."
            )

        logger.info(f"Student with ID {id} soft deleted successfully.")
        return

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error deleting student with ID {id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

@student.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def post_student(request: StudentSchema):
    logger.info("Received request to create a new student.")
    try:
        role_id = RoleRepository.get_teacher_id()
        logger.info(f"Retrieved role ID for student: {role_id}")

        if role_id is None:
            logger.warning("Student role ID not found.")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student role not found.")

        user = UserModel.create_from_student_request(request=request, role_id=str(role_id))
        logger.info(f"Created user model for {request.username}")

        with Session(engine) as session:
            session.add(user)
            session.flush()

            login = LoginModel.create_from_student_request(request=request, user_id=str(user.id))
            session.add(login)

            student_entity = StudentsModel.create_from_request(request=request, user_id=str(user.id))
            session.add(student_entity)

            session.commit()

        logger.info(f"Successfully created student: {request.username}")
        return {
            "message": "Student created successfully.",
            "username": request.username,
            "password": request.password
        }

    except Exception as e:
        logger.error(f"Error creating student: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An unexpected error occurred: {str(e)}")
