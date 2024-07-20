import pytest
from app.crud import (
    save_model_to_mongodb,
    load_model_from_mongodb,
    save_label_encoder_to_mongodb,
    load_label_encoder_from_mongodb
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def test_save_and_load_model():
    model = RandomForestClassifier()
    label_encoder = LabelEncoder()

    save_model_to_mongodb(model)
    save_label_encoder_to_mongodb(label_encoder)

    loaded_model = load_model_from_mongodb()
    loaded_label_encoder = load_label_encoder_from_mongodb()

    assert isinstance(loaded_model, RandomForestClassifier)
    assert isinstance(loaded_label_encoder, LabelEncoder)
