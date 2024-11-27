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
        classrooms = ClassroomRepository().find_all()  #

        if not classrooms:
            logger.error("No active classrooms found.")
            raise HTTPException(status_code=404, detail="No active classrooms found.")

        logger.info(f"Fetched {len(classrooms)} active classrooms successfully.")

        # Convert each ClassroomModel to a dict
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
        classroom_entity = ClassroomsModel(
            name=request.name,
            type=request.type,
            capacity=request.capacity
        )

        result = ClassroomRepository().persist(classroom_entity)

        if not result:
            raise HTTPException(status_code=500, detail="Classroom could not be created.")

        return {"message": "Classroom created successfully"}

    except Exception as e:
        logger.error(f"Error creating classroom: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred while creating the classroom.")


@classroom_router.put("/{id}", status_code=status.HTTP_200_OK)
def put_classroom(request: ClassroomSchema, id: str):
    try:

        ClassroomRepository().update(
            id=id,
            request=request
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Classroom updated successfully"}
        )

    except Exception as e:
        raise e

@classroom_router.delete("/{id}")
def delete_classroom(id: str):
    try:
        ClassroomRepository().delete(
            id=id
        )

        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content={"message": "Classroom updated successfully"}
        )

    except Exception as e:
        raise e
