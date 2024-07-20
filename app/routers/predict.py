from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import predict, get_db
from app.schemas import Iris
from typing import List

router = APIRouter()

@router.post("/predict/")
def predict_flower(data: List[Iris], db: Session = Depends(get_db)):
    features = [[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width] for iris in data]
    predictions = predict(features)
    return {"predictions": predictions}
