
import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

import urllib.request as request
import zipfile

from heart_disease_pred.entity.config_entity import DataIngestionConfig




class DataIngestion:
    def __init__(
        self,
        config: DataIngestionConfig):
    
        self.config = config

    def download_file(self):
            if not os.path.exists(self.config.data_file):
                filename, headers = request.urlretrieve(
                    url = self.config.data_url,
                    filename = self.config.data_file
                )

                logger.info(f"{filename} download! with following info: \n {headers}")

            else:
                logger.info(f"File already exists.")


    def extract_zip_file(self):
            """
            zip_file_pah: str
            Extarcts the zip file into the  data directory 
            Function return None
            """
            unzip_path = self.config.root_dir
            os.makedirs(unzip_path,exist_ok=True)
            # logger.info(f"{self.config.local_data_file}")
            with zipfile.ZipFile(self.config.data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info(f"{self.config.data_file} unzipped to {unzip_path}")  

    
