import pandas as pd

import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.constants import *
from heart_disease_pred.utils.commom import create_directories, read_yaml

from heart_disease_pred.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(
        self,
        config: DataValidationConfig):
        self.config = config

    
    def validate_all_columns(self):

        valid_status = None

        df = pd.read_csv(self.config.data_file)
        cols = df.columns

        df = df.drop('Unnamed: 0',axis=1)

        all_cols = list(self.config.all_cols.keys())

        target_col = list(self.config.target_col.keys())[0]

        all_cols.append(target_col)

        try:
            for col in cols:
                if col  not in all_cols :
                    valid_status = False
                    with open(self.config.status,'w') as f:
                        f.write(f'Validaiton Status: {valid_status}')

                else:
                    valid_status = True
                    with open(self.config.status,'w') as f:
                        f.write(f'Validaiton Status: {valid_status}')
                    # break
            

        except Exception as e:
            raise CustomException(e,sys)
        



        