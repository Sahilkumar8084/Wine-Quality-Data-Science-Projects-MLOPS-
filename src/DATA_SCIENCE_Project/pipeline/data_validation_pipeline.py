from src.DATA_SCIENCE_Project.config.configuration import ConfigurationManager
from src.DATA_SCIENCE_Project.components.data_validation_components import DataValidationComponent
from src.DATA_SCIENCE_Project import logger

STAGE_NAME="Data Validation Steps"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_validation(self):
        
        try:
            cfm = ConfigurationManager()
            data_validation_config_manager = cfm.get_data_validation_config()
            data_validation_component = DataValidationComponent(data_validation_config_manager)
            data_validation_component.validate_all_data()
            logger.info("Pipeline Ran Sucesssfully ✅😭 ")
        except Exception as e:
            logger.error("Are bhia kuch Error Aaa Gaya hai Yaar....")
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        