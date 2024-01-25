import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

import pandas as pd
from box import ConfigBox

from heart_disease_pred.utils.commom import load_pickle, save_json

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from heart_disease_pred.entity.config_entity import ModelTrainingConfig


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        try: 
            train_data = pd.read_csv(self.config.train_data)
            test_data = pd.read_csv(self.config.test_data)
            target = list(self.config.target_col.keys())[0]

            y_train = train_data[target]
            X_train = train_data.drop([target], axis=1)

            y_test = test_data[target]
            X_test = test_data.drop([target], axis=1)

            # Transform the data
            transform_obj = load_pickle(self.config.trans_obj)

            X_train_trans = pd.DataFrame(
                transform_obj.fit_transform(X_train),
                columns=transform_obj.get_feature_names_out(),
            )
            X_test_trans = pd.DataFrame(
                transform_obj.transform(X_test),
                columns=transform_obj.get_feature_names_out(),
            )

            # Tranform the target data
            target_map = {"No": 0, "Yes": 1}
            y_train_trans = y_train.map(target_map)
            y_test_trans = y_test.map(target_map)

            metrics = {
                "rf": {
                    "name": ["RandomForestClassifier"],
                    # 'model_obj': [],
                    "accuracy": [],
                    "precision": [],
                    "recall_score": [],
                    "f1_score": [],
                },
                "xg": {
                    "name": ["XGBClassifier"],
                    # 'model_obj': [],
                    "accuracy": [],
                    "precision": [],
                    "recall_score": [],
                    "f1_score": [],
                },
            }

            models = {"rf": RandomForestClassifier(), "xg": XGBClassifier()}

            # metrics = ConfigBox(metrics)

            for model_name in list(models.keys()):
                model_obj = models[model_name]

                model_obj.fit(X_train_trans, y_train_trans)

                y_pred = model_obj.predict(X_test_trans)

                # metrics[model_name]['model_obj'].append(model_obj)
                metrics[model_name]["accuracy"].append(accuracy_score(y_test_trans, y_pred))
                metrics[model_name]["precision"].append(
                    precision_score(y_test_trans, y_pred)
                )
                metrics[model_name]["recall_score"].append(
                    recall_score(y_test_trans, y_pred)
                )
                metrics[model_name]["f1_score"].append(f1_score(y_test_trans, y_pred))

            save_json(Path(self.config.metrics), metrics)


        except Exception as e:
            # logging.error(e)
            raise CustomException(e,sys)