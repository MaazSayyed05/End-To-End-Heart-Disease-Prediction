import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer

from sklearn.compose import ColumnTransformer

from heart_disease_pred.utils.commom import  save_pickle

import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(
        self,
        config: DataTransformationConfig):

        self.config = config

    
    def split_data(self):
        try:

            data = pd.read_csv(self.config.data_file)

            data = data.drop(['Unnamed: 0'], axis = 1)

            train_data, test_data = train_test_split(data, test_size=0.22, random_state=42)

            train_data.to_csv(self.config.train_data, index=False)
            test_data.to_csv(self.config.test_data, index=False)
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def transform_data(self):
        try:

            train_data = pd.read_csv(self.config.train_data)
            test_data = pd.read_csv(self.config.test_data)

            # train_data = train_data.drop(['Unnamed: 0'], axis = 1)
            # test_data = test_data.drop(['Unnamed: 0'], axis = 1)

            cat_features = [col for col in train_data.columns if train_data[col].dtype == 'object']
            num_features = [col for col in train_data.columns if train_data[col].dtype != 'object']

            cat_categories = [

            ['No' , 'Yes'], 
            ['No',  'Yes'],
            ['No' , 'Yes'],
            ['No' , 'Yes'],
            ['No' 'Yes'],
            ['Female' , 'Male'],
            ['18-24',  '25-29',  '30-34',  '35-39',  '40-44' , '45-49' , '50-54',  '55-59', '60-64',  '65-69' , '70-74',  '75-79' , '80 or older'],
            ['White' , 'Black' , 'Asian' , 'American Indian/Alaskan Native',  'Hispanic','Other'],
            ['No' , 'No, borderline diabetes' , 'Yes (during pregnancy)' , 'Yes'],
            ['No',  'Yes'],
            ['Poor',  'Fair' , 'Good',  'Very good',  'Excellent'],
            ['No',  'Yes'],
            ['No' , 'Yes'],
            ['No' , 'Yes'],

            ]

            num_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinal_encoder', OrdinalEncoder(categories=cat_categories))
                ]
            )


            transform_data = ColumnTransformer([
                ('num_pipeline', num_pipeline, num_features),
                ('cat_pipeline', cat_pipeline, cat_features),
            
            ])

            save_pickle(self.config.trans_obj, transform_data)

    
        except Exception as e:
            raise CustomException(e,sys)
