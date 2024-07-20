from sklearn.ensemble import RandomForestClassifier
import joblib
from app.database import fs
from sklearn.preprocessing import LabelEncoder
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def load_model_from_mongodb():
    file_name = "model.joblib"
    file = fs.find_one({'filename': file_name})
    if file:
        with open(file_name, 'wb') as f:
            f.write(file.read())
        model = joblib.load(file_name)
        return model
    return RandomForestClassifier()

def save_model_to_mongodb(model):
    file_name = "model.joblib"
    with open(file_name, 'wb') as f:
        joblib.dump(model, f)
    with open(file_name, 'rb') as f:
        fs.put(f, filename=file_name)

def save_label_encoder_to_mongodb(encoder):
    file_name = "label_encoder.joblib"
    with open(file_name, 'wb') as f:
        joblib.dump(encoder, f)
    with open(file_name, 'rb') as f:
        fs.put(f, filename=file_name)

def retrain_model(data, labels):
    model = load_model_from_mongodb()
    model.fit(data, labels)
    save_model_to_mongodb(model)

def predict(features):
    logger.debug(f"Features received for prediction: {features}")
    model = load_model_from_mongodb()
    prediction = model.predict(features)
    logger.debug(f"Prediction result: {prediction}")
    return str(prediction[0])
