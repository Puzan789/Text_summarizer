#pipeline

from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.config.configuration import ConfigurationManager

class DataTransformationTrainingPipeline:
    def __init__(self)->None:
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            data_transformation_config=config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e