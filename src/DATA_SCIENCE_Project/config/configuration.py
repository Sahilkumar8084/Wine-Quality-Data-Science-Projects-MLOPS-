from src.DATA_SCIENCE_Project.constants import *
from src.DATA_SCIENCE_Project.utils.helper import read_yaml,create_directories

from src.DATA_SCIENCE_Project.entity.config_entity import (DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig) #Jaab bhut sara import karna hoga too line bhut bada na ban jaye too fir hum iasa karke () isme daal sakete hia jink o hume import karna hi 


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH
                 ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])
        
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_Ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_files=config.local_data_files,
            unzip_dir=config.unzip_dir
            
        )
        
        return data_Ingestion_config
        
            
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])
        
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
            
        )
        
        return data_validation_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config =  self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config  = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config

    def get_model_trainer_config(self)-> ModelTrainerConfig:
        config =  self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir])
        model_train_config  = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_path=config.train_path,
            test_path=config.test_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
        )
        return model_train_config
    
            
    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        config =  self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])
        
        model_eval_config  = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_path=config.test_path,
            model_path = config.model_path,
            all_params= params,
            metric_file_path= config.metric_file_path,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/sahilkumarrock8084/Wine-Quality-Data-Science-Projects-MLOPS-.mlflow"
        
            
        )
        return model_eval_config

        
        