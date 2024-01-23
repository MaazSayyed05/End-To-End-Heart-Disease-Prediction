
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


