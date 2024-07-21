from fastapi import APIRouter, Depends
from app.schemas import TrainRequest, TrainResponse
from app.security import get_current_user, TokenData
from app.crud import retrain_model
import numpy as np

router = APIRouter()

@router.post("/", response_model=TrainResponse, description="Retrain the model with the provided dataset.")
async def train_model(request: TrainRequest, current_user: TokenData = Depends(get_current_user)):
    data = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width] for iris in request.data])
    labels = np.array([iris.species for iris in request.data])
    retrain_model(data, labels)
    return {"message": "Model trained successfully"}
