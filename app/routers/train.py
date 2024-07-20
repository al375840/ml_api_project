from fastapi import APIRouter
from app.schemas import TrainRequest, TrainResponse
from app.crud import retrain_model
import numpy as np

router = APIRouter()

@router.post("/", response_model=TrainResponse, description="Retrain the model with the provided dataset.")
def train_model(request: TrainRequest):
    data = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width] for iris in request.data])
    labels = np.array([iris.species for iris in request.data])
    retrain_model(data, labels)
    return {"message": "Model trained successfully"}
