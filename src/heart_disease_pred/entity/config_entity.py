
import os,sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from dataclasses import dataclass



@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    data_url: Path
    data_file: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status: Path
    data_file: Path
    all_cols: dict
    target_col: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_data: Path
    test_data: Path
    trans_obj: Path
    data_file: Path



@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data: Path
    test_data: Path
    metrics: Path
    trans_obj: Path
    target_col: Path

