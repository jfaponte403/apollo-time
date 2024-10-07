from fastapi import APIRouter, HTTPException, status

from src.models.DegreeModel import DegreeModel
from src.models.PostDegreeModel import PostDegreeModel
from src.repository.DegreeRepository import DegreeRepository

degree = APIRouter()


@degree.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def post_degree(request: PostDegreeModel):
    try:
        degree_entity = DegreeModel.create_from_request(request)
        response = DegreeRepository.persist(degree_entity)

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
