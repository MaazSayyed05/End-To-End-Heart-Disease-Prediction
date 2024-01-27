
import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

import pickle
import pandas as pd
import numpy as np

from heart_disease_pred.utils.commom import  read_yaml, load_pickle
from heart_disease_pred.constants import *


class PredictionPipeline:
    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)

    def predict(self,data):
        try:
            
            logging.info(f'Input Data: \n{data}')

            model_path, transform_path = self.config.model_training.best_model, self.config.model_training.trans_obj

            model = load_pickle(model_path)
            transform_obj = load_pickle(transform_path)

            data_transform = transform_obj.transform(data)

            predict = model.predict(data_transform)
            

            if predict == 0:
                return 'No'
            
            elif predict == 1:
                return 'Yes'

            # return predict

        except Exception as e:
            raise CustomException(e,sys)
        



