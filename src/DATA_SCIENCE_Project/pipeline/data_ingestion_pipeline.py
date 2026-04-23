from src.DATA_SCIENCE_Project.config.configuration import ConfigurationManager
from src.DATA_SCIENCE_Project.components.data_ingestion_components import DataingestionComponent
from src.DATA_SCIENCE_Project import logger


STAGE_NAME="Data Ingestion Steps"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        
        try:
            cfm = ConfigurationManager()
            data_ingestion_config_manager = cfm.get_data_ingestion_config()
            data_ingestion_component = DataingestionComponent(data_ingestion_config_manager)
            data_ingestion_component.download_data()
            # data_ingestion_component.extract_zip_file()
            logger.info("Pipeline Ran Sucesssfully ✅😭 ")
        except Exception as e:
            logger.error("Are bhia kuch Error Aaa Gaya hai Yaar....")
            raise e
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e