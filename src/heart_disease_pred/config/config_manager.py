import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.constants import *
from heart_disease_pred.utils.commom import create_directories, read_yaml

from heart_disease_pred.entity.config_entity import DataIngestionConfig
from heart_disease_pred.entity.config_entity import DataValidationConfig
from heart_disease_pred.entity.config_entity import DataTransformationConfig
from heart_disease_pred.entity.config_entity import ModelTrainingConfig

import pandas as pd


class ConfigManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, schema_file_path=SCHEMA_FILE_PATH):

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


    def get_data_validation_config(self) -> DataValidationConfig:
            config = self.config.data_validation
            schema_cols = self.schema.features
            schema_target = self.schema.target

            create_directories([config.root_dir])

            data_validation_config = DataValidationConfig(
                root_dir = Path(config.root_dir),
                status = Path(config.status),
                data_file = Path(config.data_file),
                all_cols = schema_cols,
                target_col = schema_target
            )

            return data_validation_config



    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            train_data=config.train_data,
            test_data=config.test_data,
            trans_obj=config.trans_obj,
            data_file=config.data_file
        )

        return data_transformation_config

    
    
    def get_model_training_config(self) -> ModelTrainingConfig:

        config = self.config.model_training
        schema = self.schema
        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir = config.root_dir,
            train_data = config.train_data,
            test_data = config.test_data,
            metrics = config.metrics,
            trans_obj = config.trans_obj,
            best_model = config.best_model,
            target_col = schema.target
        )

        return model_training_config