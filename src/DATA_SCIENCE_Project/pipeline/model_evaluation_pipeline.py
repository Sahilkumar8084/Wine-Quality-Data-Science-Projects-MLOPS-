from src.DATA_SCIENCE_Project.config.configuration import ConfigurationManager
from src.DATA_SCIENCE_Project.components.model_evaluation_component import ModelEvaluationComponent
from src.DATA_SCIENCE_Project import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        
        try:
            
            cfm = ConfigurationManager()
            model_evaluate_manager = cfm.get_model_evaluation_config()
            model_evaluate_component = ModelEvaluationComponent(model_evaluate_manager)
            model_evaluate_component.log_into_mlflow()
            logger.info("Pipeline Ran Sucesssfully ✅😭 ")
        except Exception as e:
            logger.error("Are bhia kuch Error Aaa Gaya hai Yaar....")
            logger.error(e)
            raise e
        
if __name__ == "__main__":
    try:
        STAGE_NAME="MODEL EVALUATION"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        obj = ModelEvaluationTrainingPipeline()
        obj.initiate_model_evaluation() # .main() call karna mat bhulna jo humne pipeline mein banaya hai
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        