import gridfs
import joblib
from pymongo import MongoClient
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import os
import io

DATABASE_URL = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = "ml_api_db"

client = MongoClient(DATABASE_URL)
db = client[DATABASE_NAME]
fs = gridfs.GridFS(db)

def save_model_to_mongodb(model, file_name="model.joblib"):
    buffer = io.BytesIO()
    joblib.dump(model, buffer)
    buffer.seek(0)
    with fs.new_file(filename=file_name) as fp:
        fp.write(buffer.read())

def load_model_from_mongodb(file_name="model.joblib"):
    file = fs.find_one({'filename': file_name})
    if file:
        buffer = io.BytesIO(file.read())
        buffer.seek(0)
        model = joblib.load(buffer)
        return model
    else:
        raise FileNotFoundError(f"No model found with filename {file_name}")

def save_label_encoder_to_mongodb(label_encoder, file_name="label_encoder.joblib"):
    buffer = io.BytesIO()
    joblib.dump(label_encoder, buffer)
    buffer.seek(0)
    with fs.new_file(filename=file_name) as fp:
        fp.write(buffer.read())

def load_label_encoder_from_mongodb(file_name="label_encoder.joblib"):
    file = fs.find_one({'filename': file_name})
    if file:
        buffer = io.BytesIO(file.read())
        buffer.seek(0)
        label_encoder = joblib.load(buffer)
        return label_encoder
    else:
        raise FileNotFoundError(f"No label encoder found with filename {file_name}")

def retrain_model(new_data, new_labels):
    model = load_model_from_mongodb()
    model.fit(new_data, new_labels)
    save_model_to_mongodb(model)
    return model

def predict(data):
    model = load_model_from_mongodb()
    predictions = model.predict(data)
    return predictions

def get_db():
    return db
