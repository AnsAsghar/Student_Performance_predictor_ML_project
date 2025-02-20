import os
import sys
import pymysql
import pandas as pd
from dotenv import load_dotenv
from src.ml_project_1.exception import CustomException
from src.ml_project_1.logger import logging

load_dotenv()

host = os.getenv("host", "localhost")
user = os.getenv("user", "root")
password = os.getenv("password", "")
db = os.getenv("db", "college")

def get_db_connection():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        logging.info("Database connection established successfully")
        return connection
    except Exception as e:
        error_message = f"Error connecting to database: {str(e)}"
        logging.error(error_message)
        raise CustomException(error_message, sys)