from fastapi import FastAPI
from app.routers import train, predict

app = FastAPI(
    title="ML API Project",
    description="This is an API for training and predicting machine learning models using the Iris dataset.",
    version="1.0.0",
    contact={
        "name": "Adrián León Alonso",
        "url": "https://github.com/al375840/ml_api_project",
    },
)

app.include_router(train.router, prefix="/train", tags=["train"])
app.include_router(predict.router, prefix="/predict", tags=["predict"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML API"}

