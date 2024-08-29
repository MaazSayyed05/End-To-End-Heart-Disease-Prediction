
from flask import Flask, render_template, request
import os , sys
import numpy as np
import pandas as pd

from heart_disease_pred.pipeline.prediction import PredictionPipeline
from heart_disease_pred.pipeline.database import mysqlconnect

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:

            # -----------------------------------------------------------------------

            BMI             = float(request.form['BMI'])
            Smoking         = str(request.form['Smoking'])
            AlcoholDrinking = str(request.form['AlcoholDrinking'])
            Stroke          = str(request.form['Stroke'])
            PhysicalHealth  = float(request.form['PhysicalHealth'])
            MentalHealth    = float(request.form['MentalHealth'])
            DiffWalking     = str(request.form['DiffWalking'])
            Sex             = str(request.form['Sex'])
            AgeCategory     = str(request.form['AgeCategory'])
            Race            = str(request.form['Race'])
            Diabetic        = str(request.form['Diabetic'])
            PhysicalActivity= str(request.form['PhysicalActivity'])
            GenHealth       = str(request.form['GenHealth'])
            SleepTime       = float(request.form['SleepTime'])
            Asthma          = str(request.form['Asthma'])
            KidneyDisease   = str(request.form['KidneyDisease'])
            SkinCancer      = str(request.form['SkinCancer'])

            # -----------------------------------------------------------------------

            data = [BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer]
            data = np.array(data).reshape(1, 17)
            data = pd.DataFrame(data)
            data.columns = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth', 'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease', 'SkinCancer']
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            # ----------------------------------------------------------------
            mysql_pipeline = mysqlconnect()
            mysql_pipeline.insert_data(data,predict)
            # ----------------------------------------------------------------
            
            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            # print('The Exception message is: ',e)
            raise CustomException(e,sys)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 88, debug=True)
	app.run(host="0.0.0.0", port = 88)






# HeartDisease =      ['No' , 'Yes'] 
# Smoking =           ['No',  'Yes']
# AlcoholDrinking =   ['No' , 'Yes']
# Stroke =            ['No' , 'Yes']
# DiffWalking =       ['No' 'Yes']
# Sex =               ['Female' , 'Male']
# AgeCategory =       ['18-24',  '25-29',  '30-34',  '35-39',  '40-44' , '45-49' , '50-54',  '55-59', '60-64',  '65-69' , '70-74',  '75-79' , '80 or older']
# Race =              ['White' , 'Black' , 'Asian' , 'American Indian/Alaskan Native',  'Hispanic','Other']
# Diabetic =          ['No' , 'No, borderline diabetes' , 'Yes (during pregnancy)' , 'Yes']
# PhysicalActivity =  ['No',  'Yes']
# GenHealth =         ['Poor',  'Fair' , 'Good',  'Very good',  'Excellent']
# Asthma =            ['No',  'Yes']
# KidneyDisease =     ['No' , 'Yes']
# SkinCancer =        ['No' , 'Yes']