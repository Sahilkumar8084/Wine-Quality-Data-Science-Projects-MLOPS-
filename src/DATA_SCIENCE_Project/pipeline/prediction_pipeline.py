import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class Prediction_Pipeline:
    def __init__(self):
        self.model = joblib.load(Path(r"artifacts\model_trainer\model.joblib"))
        
    def prediction(self,data):
        predict = self.model.predict(data)
        
        return predict
    

        