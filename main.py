import logging
from src.DATA_SCIENCE_Project import logger
from src.DATA_SCIENCE_Project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

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