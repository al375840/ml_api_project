from pydantic import BaseModel
from typing import List

class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str

    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
                "species": "setosa"
            }
        }

class TrainRequest(BaseModel):
    data: List[Iris]

    class Config:
        schema_extra = {
            "example": {
                "data": [
                    {
                        "sepal_length": 5.1,
                        "sepal_width": 3.5,
                        "petal_length": 1.4,
                        "petal_width": 0.2,
                        "species": "setosa"
                    },
                    {
                        "sepal_length": 7.0,
                        "sepal_width": 3.2,
                        "petal_length": 4.7,
                        "petal_width": 1.4,
                        "species": "versicolor"
                    }
                ]
            }
        }

class TrainResponse(BaseModel):
    message: str

    class Config:
        schema_extra = {
            "example": {
                "message": "Model trained successfully"
            }
        }

class PredictRequest(BaseModel):
    data: Iris

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "sepal_length": 5.1,
                    "sepal_width": 3.5,
                    "petal_length": 1.4,
                    "petal_width": 0.2,
                    "species": "?"
                }
            }
        }

class PredictResponse(BaseModel):
    prediction: str

    class Config:
        schema_extra = {
            "example": {
                "prediction": "setosa"
            }
        }
