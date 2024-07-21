from fastapi import APIRouter, Depends
from app.schemas import PredictRequest, PredictResponse
from app.security import get_current_user, TokenData
from app.crud import predict
import numpy as np

router = APIRouter()

@router.post("/", response_model=PredictResponse, description="Predict the class of an iris flower based on the provided features.")
async def predict_flower(request: PredictRequest, current_user: TokenData = Depends(get_current_user)):
    features = np.array([[request.data.sepal_length, request.data.sepal_width, request.data.petal_length, request.data.petal_width]])
    prediction = predict(features)
    return {"prediction": prediction}
