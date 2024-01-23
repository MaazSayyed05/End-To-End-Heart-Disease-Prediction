
import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log" #NAme of log file

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) # create logs folder in current working directory
os.makedirs(logs_path,exist_ok=True) # if folder exist then no need to create new folder

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)
