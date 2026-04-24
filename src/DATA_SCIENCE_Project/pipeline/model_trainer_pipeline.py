from src.DATA_SCIENCE_Project.config.configuration import ConfigurationManager
from src.DATA_SCIENCE_Project.components.model_trainer_component import ModelTrainerComponent
from src.DATA_SCIENCE_Project import logger
from pathlib import Path

STAGE_NAME="Model Trainer Steps"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
        
        try:
            cfm = ConfigurationManager()
            model_trainer_manager = cfm.get_model_trainer_config()
            model_trainer_component = ModelTrainerComponent(model_trainer_manager)
            model_trainer_component.train()
            logger.info("Pipeline Ran Sucesssfully ✅😭 ")
        except Exception as e:
            logger.error("Are bhia kuch Error Aaa Gaya hai Yaar....")
            logger.error(e)
            raise e
                
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_trainer() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        