from textSummarizer.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from textSummarizer.utils.common import read_yaml ,create_directories
from pathlib import Path
from textSummarizer.entity import (DataIngestionConfig,DatavalidationConfig,DataTransformConfig,ModelTrainingConfig,ModelEvaluationConfig)


class ConfigurationManager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([Path(config.root_dir)])  # Ensure it's a Path object
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),  # Convert to Path object
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),  # Convert to Path object
            unzip_dir=Path(config.unzip_dir),  # Convert to Path object
        )
        return data_ingestion_config

    def get_data_validation_config(self):
        config=self.config.data_validation
        create_directories([config.root_dir])
        data_validation_config=DatavalidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformConfig:
        config=self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config=DataTransformConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainingConfig:
        config=self.config.model_trainer
        params=self.params.TrainingArguments

        model_trainer_config=ModelTrainingConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )

        return model_evaluation_config