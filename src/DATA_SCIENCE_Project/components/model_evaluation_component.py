import os
from src.DATA_SCIENCE_Project import logger
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import mlflow
import mlflow.sklearn
import numpy as np
from urllib.parse import urlparse

from src.DATA_SCIENCE_Project.entity.config_entity import ModelEvaluationConfig
from src.DATA_SCIENCE_Project.utils.helper import read_yaml,create_directories,save_json
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

class ModelEvaluationComponent:
        def __init__(self,config:ModelEvaluationConfig):
            self.config = config
            
        def eval_metrics(self,actual,pred):
            rmse = np.sqrt(mean_squared_error(actual,pred))
            mae = mean_absolute_error(actual,pred)
            r2 = r2_score(actual,pred)
            
            return rmse,mae,r2
        def log_into_mlflow(self):
            test_data = pd.read_csv(self.config.test_path)
            
            print(test_data.columns)
            
            model = joblib.load(self.config.model_path)
            print("Col: ",self.config.target_column)
            
            test_x = test_data.drop([self.config.target_column],axis=1)
            test_y = test_data[[self.config.target_column]]
            
            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_uri_type_story = urlparse(mlflow.get_tracking_uri()).scheme
            
            with mlflow.start_run():
                
                prediction = model.predict(test_x)   
                
                (rmse,mae,r2) = self.eval_metrics(test_y,prediction) 
                scores = {'RMSE':rmse,'MAE':mae,'R2':r2} 
                
                save_json(path= Path(self.config.metric_file_path),data=scores) 
                
                mlflow.log_params(self.config.all_params)
                
                mlflow.log_metrics(scores)
                
                if tracking_uri_type_story != 'file':
                    
                    mlflow.sklearn.log_model(model, "model")
                else:
                    mlflow.sklearn.log_model(model,"model")
                    
            
            


