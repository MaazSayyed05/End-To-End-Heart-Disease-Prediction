
import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.config.config_manager import ConfigManager

from heart_disease_pred.components.model_training import ModelTraining

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigManager()
            model_training_config = config.get_model_training_config()
            model_trainer = ModelTraining(model_training_config)

            model_trainer.train()

        except Exception as e:
            raise CustomException(e,sys)


