from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_datavalidation import DataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_04_modeltrainer import ModelTrainingPipeline
from src.textSummarizer.pipeline.stage_05_modelevaluation import ModelEvaluationTrainingPipeline


from src.textSummarizer.logging import logger 

STAGE_NAME ="DATA INGESTION STAGE"
try:
    logger.info(f"<><><> stage {STAGE_NAME} started <><><>")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<><><> stage {STAGE_NAME} completed successfully <><><>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME ="DATA VALIDATION STAGE"
try:
    logger.info(f"<><><> stage {STAGE_NAME} started <><><>")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"<><><> stage {STAGE_NAME} completed successfully <><><>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME ="DATA TRANSFORMATION STAGE"
try:
    logger.info(f"<><><> stage {STAGE_NAME} started <><><>")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"<><><> stage {STAGE_NAME} completed successfully <><><>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME ="MODEL TRAINING STAGE"
try:
    logger.info(f"<><><> stage {STAGE_NAME} started <><><>")
    model_training=ModelTrainingPipeline()
    model_training.main()
    logger.info(f"<><><> stage {STAGE_NAME} completed successfully <><><>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e