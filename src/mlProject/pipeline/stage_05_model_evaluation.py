from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger
import os 
import mlflow
STAGE_NAME = "Model evaluation stage"
os.environ["MLFLOW_TRACKING_USERNAME"]="ajinkyaprabhuds-sys"
os.environ["MLFLOW_TRACKING_PASSWORD"]="5c4ad9682c4a5cc52d534fe17edffe5045757f1b"

mlflow.set_tracking_uri("https://dagshub.com/ajinkyaprabhuds-sys/End-to-end-ML-Project-with-MLflow.mlflow")


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

