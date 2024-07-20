import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
from app.crud import save_model_to_mongodb, save_label_encoder_to_mongodb

dataset_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/IRIS.csv'

def pretrain_model():
    data = pd.read_csv(dataset_path)

    X = data.drop(columns=['species'])
    y = data['species']

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    save_model_to_mongodb(model)
    save_label_encoder_to_mongodb(label_encoder)

if __name__ == "__main__":
    pretrain_model()
