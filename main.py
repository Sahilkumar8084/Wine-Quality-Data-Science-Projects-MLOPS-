import logging
from src.DATA_SCIENCE_Project import logger
from src.DATA_SCIENCE_Project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DATA_SCIENCE_Project.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DATA_SCIENCE_Project.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DATA_SCIENCE_Project.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.DATA_SCIENCE_Project.pipeline.model_evaluation_pipeline import ModelEvaluationComponent
from src.DATA_SCIENCE_Project.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline


if __name__ == "__main__":
    try:
        STAGE_NAME = "Data Ingestion stage" # Stage name define karna zaroori hai
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

    try:
        STAGE_NAME = "Data Validation stage" # Stage name define karna zaroori hai
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation() 
        
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    try:
        STAGE_NAME = "Data Transformation stage" # Stage name define karna zaroori hai

        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    
    try:
        STAGE_NAME = "Model Trainer stage" # Stage name define karna zaroori hai

        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_trainer() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    
    try:
        STAGE_NAME="MODEL EVALUATION"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = ModelEvaluationTrainingPipeline()
        obj.initiate_model_evaluation() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        