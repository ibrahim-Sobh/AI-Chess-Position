from statistics import mode
from keras.models import load_model
import app.preprocess as preprocessing

MODEL_PATH='../models/perfect_model.h5'

def make_prediction(input_image_path: str) -> str:
    # load the model
    model= load_model(MODEL_PATH)
    img_label=preprocessing.get_image_FEN_label(input_image_path)
    y = preprocessing.onehot_from_fen(img_label)
    x = preprocessing.preprocess_image(input_image_path)
    res = (model.predict(x).argmax(axis=1) .reshape(-1, 8, 8))
    prediciton= preprocessing.fen_from_onehot(res[0])
    return prediciton
