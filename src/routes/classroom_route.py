from fastapi import APIRouter, HTTPException, status
import logging

from fastapi.responses import JSONResponse

from src.models.ClassroomsModel import ClassroomsModel
from src.repository.ClassroomRepository import ClassroomRepository
from src.schemas.ClassroomSchema import ClassroomSchema

classroom_router = APIRouter()
logger = logging.getLogger(__name__)


@classroom_router.get("/", status_code=status.HTTP_200_OK)
def get_classrooms():
    logger.info("Received request to fetch all active classrooms.")
    try:
        classrooms = ClassroomRepository().find_all()

        if not classrooms:
            logger.error("No active classrooms found.")
            raise HTTPException(status_code=404, detail="No active classrooms found.")

        logger.info(f"Fetched {len(classrooms)} active classrooms successfully.")

        classrooms_data = [classroom.to_dict() for classroom in classrooms]

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"classrooms": classrooms_data}
        )
    except Exception as e:
        logger.error(f"Error fetching classrooms: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching classrooms.")


@classroom_router.post("/", status_code=status.HTTP_201_CREATED)
def post_classroom(request: ClassroomSchema):
    try:
        classroom_entity = ClassroomsModel(**request.dict())
        result = ClassroomRepository().persist(classroom_entity)

        if not result:
            raise HTTPException(status_code=500, detail="Classroom could not be created.")

        return {"message": "Classroom created successfully"}

    except Exception as e:
        logger.error(f"Error creating classroom: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred while creating the classroom.")


@classroom_router.put("/{classroom_id}", status_code=status.HTTP_200_OK)
def update_classroom(classroom_id: str, request: ClassroomSchema):
    try:
        logger.info(f"Received request to update classroom with ID: {classroom_id}")

        classroom_entity = ClassroomsModel(id=classroom_id, **request.dict(exclude_unset=True))
        result = ClassroomRepository().update(classroom_entity)

        if not result:
            logger.error(f"Classroom with ID {classroom_id} could not be updated or was not found.")
            raise HTTPException(status_code=404, detail="Classroom not found or could not be updated.")

        return {"message": "Classroom updated successfully"}

    except Exception as e:
        logger.error(f"Error updating classroom with ID {classroom_id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred while updating the classroom.")


@classroom_router.delete("/{classroom_id}", status_code=status.HTTP_200_OK)
def delete_classroom(classroom_id: str):
    try:
        logger.info(f"Received request to delete classroom with ID: {classroom_id}")

        result = ClassroomRepository().delete(classroom_id)

        if not result:
            logger.error(f"Classroom with ID {classroom_id} could not be deleted or was not found.")
            raise HTTPException(status_code=404, detail="Classroom not found or could not be deleted.")

        return {"message": "Classroom deleted successfully"}

    except Exception as e:
        logger.error(f"Error deleting classroom with ID {classroom_id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred while deleting the classroom.")
