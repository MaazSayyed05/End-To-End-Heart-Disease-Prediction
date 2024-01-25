import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

from heart_disease_pred.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from heart_disease_pred.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from heart_disease_pred.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from heart_disease_pred.pipeline.stage_04_model_training import ModelTrainingPipeline

stage_name = "Data Ingestion"
try:
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Started <<<<<<<<<<<<<<<<<<< ")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Completed <<<<<<<<<<<<<<<<<<< ")

except Exception as e:
    logging.error(f">>>>>>>>>>>>>>>>> {stage_name} Failed <<<<<<<<<<<<<<<<<<< ")
    raise CustomException(e,sys)




stage_name = "Data Validation"
try:
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Started <<<<<<<<<<<<<<<<<<< ")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Completed <<<<<<<<<<<<<<<<<<< ")

except Exception as e:
    logging.error(f">>>>>>>>>>>>>>>>> {stage_name} Failed <<<<<<<<<<<<<<<<<<< ")
    raise CustomException(e,sys)





stage_name = "Data Transformation"
try:
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Started <<<<<<<<<<<<<<<<<<< ")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Completed <<<<<<<<<<<<<<<<<<< ")

except Exception as e:
    logging.error(f">>>>>>>>>>>>>>>>> {stage_name} Failed <<<<<<<<<<<<<<<<<<< ")
    raise CustomException(e,sys)






stage_name = "Model Training"
try:
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Started <<<<<<<<<<<<<<<<<<< ")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Completed <<<<<<<<<<<<<<<<<<< ")

except Exception as e:
    logging.error(f">>>>>>>>>>>>>>>>> {stage_name} Failed <<<<<<<<<<<<<<<<<<< ")
    raise CustomException(e,sys)


