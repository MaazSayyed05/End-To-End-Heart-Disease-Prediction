import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.config.config_manager import ConfigManager

from heart_disease_pred.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            # data_ingestion.download_file()
            # data_ingestion.extract_zip_file()
            

        except Exception as e:
            raise CustomException(e,sys)