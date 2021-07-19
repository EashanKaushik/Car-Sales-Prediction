from pickle import load
from tensorflow.keras.models import load_model
import pandas as pd

MODEL_PATH = 'model/model.h5'
SCALER_PATH = 'model/scaler.pkl'
SCALER_DEP_PATH = 'model/scaler_dep.pkl'

model = load_model(MODEL_PATH)
scaler = load(open(SCALER_PATH, 'rb'))
scaler_dep = load(open(SCALER_DEP_PATH, 'rb'))

def make_prediction(predict_data):
    predict_data = pd.Series(predict_data)
    predict_data = scaler.transform(predict_data.values.reshape(1,-1))

    prediction = model.predict(predict_data)

    return scaler_dep.inverse_transform(prediction)