from fastapi import APIRouter
from app.schemas import TrainRequest, TrainResponse
from app.crud import retrain_model
import numpy as np

router = APIRouter()

@router.post("/", response_model=TrainResponse)
def train_model(request: TrainRequest):
    data = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width] for iris in request.data])
    labels = request.species
    retrain_model(data, labels)
    return {"message": "Model trained successfully"}
