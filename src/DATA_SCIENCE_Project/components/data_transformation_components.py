import os
from src.DATA_SCIENCE_Project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.DATA_SCIENCE_Project.config.configuration import DataTransformationConfig

class DataTransformationComponent:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        
    def split_data(self):
        df = pd.read_csv(self.config.data_path,sep=";")
        print(df.head())
        
        train,test = train_test_split(df,test_size=0.25,random_state=42)
        logger.info("Splitted Data into Training and Test Data")
        print(train.shape)
        logger.info(f"Train Data Shape: {train.shape}")
        print(test.shape)
        logger.info(f"Test Data Shape: {test.shape}")

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)