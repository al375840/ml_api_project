from fastapi import FastAPI
from app.routers import train, predict

app = FastAPI()

app.include_router(train.router, prefix="/train", tags=["train"])
app.include_router(predict.router, prefix="/predict", tags=["predict"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML API"}

