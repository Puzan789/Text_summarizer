from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_datavalidation import DataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline


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