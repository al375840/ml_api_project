from pydantic import BaseModel
from typing import List

class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class TrainRequest(BaseModel):
    data: List[Iris]
    species: List[str]

class TrainResponse(BaseModel):
    message: str

class PredictRequest(BaseModel):
    data: Iris

class PredictResponse(BaseModel):
    prediction: str
