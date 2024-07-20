import joblib
from app.database import fs
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

def save_model_to_mongodb(model, collection_name='models', file_name='model.joblib'):
    with open(file_name, 'wb') as f:
        joblib.dump(model, f)
    with open(file_name, 'rb') as f:
        fs.put(f, filename=file_name)

def load_model_from_mongodb(file_name='model.joblib'):
    file = fs.find_one({'filename': file_name})
    if file:
        with open(file_name, 'wb') as f:
            f.write(file.read())
        model = joblib.load(file_name)
        return model
    return None

def save_label_encoder_to_mongodb(label_encoder, file_name='label_encoder.joblib'):
    with open(file_name, 'wb') as f:
        joblib.dump(label_encoder, f)
    with open(file_name, 'rb') as f:
        fs.put(f, filename=file_name)

def load_label_encoder_from_mongodb(file_name='label_encoder.joblib'):
    file = fs.find_one({'filename': file_name})
    if file:
        with open(file_name, 'wb') as f:
            f.write(file.read())
        label_encoder = joblib.load(file_name)
        return label_encoder
    return None

model = load_model_from_mongodb()
label_encoder = load_label_encoder_from_mongodb()

if model is None:
    model = RandomForestClassifier(n_estimators=100, random_state=42)

if label_encoder is None:
    label_encoder = LabelEncoder()

def retrain_model(new_data: np.ndarray, new_labels: list):
    global model
    new_labels_encoded = label_encoder.fit_transform(new_labels)
    model.fit(new_data, new_labels_encoded)
    save_model_to_mongodb(model)
    save_label_encoder_to_mongodb(label_encoder)
    return model

def predict(data: np.ndarray):
    global model
    prediction = model.predict(data)
    return label_encoder.inverse_transform(prediction)
