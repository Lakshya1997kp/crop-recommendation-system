from flask import Flask, render_template
import numpy as np
import joblib
import sklearn 

model=joblib.load("model.pkl")

def ml_prediction(features):
    features=[np.array(features)]

    # predicting the value

    prediction=model.predict(features)

    return prediction[0]