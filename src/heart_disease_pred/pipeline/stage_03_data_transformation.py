import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.config.config_manager import ConfigManager

from heart_disease_pred.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)

            data_transformation.split_data()

            data_transformation.transform_data()
        
        except Exception as e:
            raise CustomException(e,sys)


