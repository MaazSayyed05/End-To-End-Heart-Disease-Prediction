CREATE DATABASE IF NOT EXISTS projects;

USE projects;

CREATE TABLE IF NOT EXISTS  heart(
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
);


INSERT INTO heart 
(BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity,  GenHealth,  SleepTime,  Asthma,  KidneyDisease,  SkinCancer, HeartDisease)
VALUES 
(16.34, 'No', 'No', 'No', 0, 20, 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 5, 'No', 'Yes', 'Yes', 'No');


SELECT * FROM heart;

DROP TABLE heart;