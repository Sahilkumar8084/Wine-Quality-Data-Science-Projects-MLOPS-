from src.DATA_SCIENCE_Project.config.configuration import ConfigurationManager
from src.DATA_SCIENCE_Project.components.data_transformation_components import DataTransformationComponent
from src.DATA_SCIENCE_Project import logger
from pathlib import Path

STAGE_NAME="Data Transformation Steps"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        
        try:
            
            with open(Path("artifacts\data_validation\status.txt"),'r') as f:
                cnt = f.readlines()[-1].split(" ")
                print(cnt[-1])
                if cnt[-1]:
    
                    cfm = ConfigurationManager()
                    data_transformation_config_manager = cfm.get_data_transformation_config()
                    data_transformation_component = DataTransformationComponent(data_transformation_config_manager)
                    data_transformation_component.split_data()
                    logger.info("Pipeline Ran Sucesssfully ✅😭 ")
                else:
                    raise Exception("Are bhia kuch Error Aaa Gaya hai Yaar....")
        except Exception as e:
            logger.error("❌There is some issue While Reading the File")
            print(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        