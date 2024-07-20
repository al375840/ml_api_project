from fastapi import APIRouter
from app.schemas import PredictRequest, PredictResponse
from app.crud import predict
import numpy as np

router = APIRouter()

@router.post("/", response_model=PredictResponse)
def predict_model(request: PredictRequest):
    data = np.array([[request.data.sepal_length, request.data.sepal_width, request.data.petal_length, request.data.petal_width]])
    prediction = predict(data)
    return {"prediction": prediction[0]}
