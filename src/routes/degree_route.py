from fastapi import APIRouter, HTTPException, status

from src.models.DegreeModel import DegreeModel
from src.schemas.DegreeSchema import DegreeSchema
from src.repository.DegreeRepository import DegreeRepository

degree = APIRouter()


@degree.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def post_degree(request: DegreeSchema):
    try:
        degree_entity = DegreeModel.create_from_request(request)
        response = DegreeRepository().persist(degree_entity)

        if response:
            return {"message": "Degree created successfully."}

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to create degree due to a database error."
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )


@degree.get("/", response_model=dict)
def get_degrees():
    try:
        degrees = DegreeRepository().find_all()

        if degrees is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No degrees found."
            )

        return {"degrees": degrees}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )