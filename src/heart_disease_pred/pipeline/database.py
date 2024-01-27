import mysql.connector
import os, sys
from pathlib import Path
from heart_disease_pred.logger import logging
from heart_disease_pred.exception import CustomException

class mysqlconnect:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "8767M@@z052003"

        self.mydb = mysql.connector.connect(
            host = host, 
            user = user, 
            password = password)

    
    def insert_data(self,data,predicted):
        try:
                
            mycursor = self.mydb.cursor()

            database = "projects"
            table = "heart"

            mycursor.execute(f'CREATE DATABASE IF NOT EXISTS {database};')
            mycursor.execute(f'USE {database};')

            mycursor.execute(f'''CREATE TABLE IF NOT EXISTS  {table} 
            (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    BMI FLOAT,
                    Smoking VARCHAR(30),
                    AlcoholDrinking VARCHAR(30),
                    Stroke VARCHAR(30),
                    PhysicalHealth FLOAT,
                    MentalHealth FLOAT,
                    DiffWalking VARCHAR(30),
                    Sex VARCHAR(30),
                    AgeCategory VARCHAR(30),
                    Race VARCHAR(30),
                    Diabetic VARCHAR(30),
                    PhysicalActivity VARCHAR(30),
                    GenHealth VARCHAR(30),
                    SleepTime FLOAT,
                    Asthma VARCHAR(30),
                    KidneyDisease VARCHAR(30),
                    SkinCancer VARCHAR(30),
                    HeartDisease VARCHAR(30)
                );'''
            )

            insert = f'INSERT INTO {database}.{table} (BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity,  GenHealth,  SleepTime,  Asthma,  KidneyDisease,  SkinCancer, HeartDisease) VALUES ({data["BMI"].iloc[0]},"{data["Smoking"].iloc[0]}","{data["AlcoholDrinking"].iloc[0]}","{data["Stroke"].iloc[0]}",{data["PhysicalHealth"].iloc[0]},{data["MentalHealth"].iloc[0]},"{data["DiffWalking"].iloc[0]}","{data["Sex"].iloc[0]}","{data["AgeCategory"].iloc[0]}","{data["Race"].iloc[0]}","{data["Diabetic"].iloc[0]}","{data["PhysicalActivity"].iloc[0]}","{data["GenHealth"].iloc[0]}",{data["SleepTime"].iloc[0]},"{data["Asthma"].iloc[0]}","{data["KidneyDisease"].iloc[0]}","{data["SkinCancer"].iloc[0]}","{predicted}");'

            logging.info(insert)

            mycursor.execute(insert)

            # Show table
            # mycursor.execute("SELECT * FROM {database}.{table};")
            # logging.info("Data : \n") 
            # # Printing data of table 'record_2'
            # for row in mycursor :
            #     logging.info(row)
                        
            self.mydb.commit()

            self.mydb.close()

        except Exception as e:
            raise CustomException(e,sys)




        
