import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.config.config_manager import ConfigManager

from heart_disease_pred.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigManager()
            data_validation = DataValidation(config.get_data_validation_config())
            status = data_validation.validate_all_columns()
            # logging.info(f'Validation Status: {status}')
        
        except Exception as e:
            raise CustomException(e,sys)


