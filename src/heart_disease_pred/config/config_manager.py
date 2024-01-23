import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.constants import *
from heart_disease_pred.utils.commom import create_directories, read_yaml

from heart_disease_pred.entity.config_entity import DataIngestionConfig


class ConfigManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, schema_file_path=SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            data_url=config.data_url,
            data_file=config.data_file,
        )

        return data_ingestion_config
