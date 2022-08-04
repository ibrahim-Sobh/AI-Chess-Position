from statistics import mode

import app.preprocess as preprocessing
from keras.models import load_model


MODEL_PATH='models/perfect_model.h5'

def make_prediction(input_image_path: str) -> str:
    # load the model
    model= load_model(MODEL_PATH)
    x = preprocessing.preprocess_image(input_image_path)
    res = (model.predict(x).argmax(axis=1) .reshape(-1, 8, 8))
    prediciton= preprocessing.fen_from_onehot(res[0])
    return prediciton
