import os
from src.DATA_SCIENCE_Project import logger
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import pandas as pd
import joblib
from src.DATA_SCIENCE_Project.config.configuration import ModelTrainerConfig

class ModelTrainerComponent:
        def __init__(self,config:ModelTrainerConfig):
            self.config = config
        
        def train(self):
            
            # 1. Load the data properly
            train_data = pd.read_csv(self.config.train_path)
            test_data = pd.read_csv(self.config.test_path)

            # 2. Split Features (X) and Target (y)
            tar = self.config.target_column
            print(tar)
            train_x = train_data.drop([tar], axis=1)
            test_x = test_data.drop([tar], axis=1)
            
            train_y = train_data[[tar]]
            test_y = test_data[[tar]]

            # 3. Model Initialization and Training
            # Fixed typos: alpha and l1_ratio
            lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
            lr.fit(train_x, train_y)

            # 4. Save the Model
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(lr, model_path)
            
        
    