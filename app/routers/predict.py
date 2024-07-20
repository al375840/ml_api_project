from fastapi import APIRouter, Depends, HTTPException
from app.crud import predict
from app.schemas import PredictRequest, PredictResponse

router = APIRouter()

@router.post("/", response_model=PredictResponse, description="Predict the class of an iris flower based on the provided features.")
def predict_flower(request: PredictRequest):
    features = [[request.data.sepal_length, request.data.sepal_width, request.data.petal_length, request.data.petal_width]]
    prediction = predict(features)
    return {"prediction": prediction}
