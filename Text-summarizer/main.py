from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_datavalidation import DataValidationTrainingPipeline

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
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<><><> stage {STAGE_NAME} completed successfully <><><>")
except Exception as e:
    logger.exception(e)
    raise e