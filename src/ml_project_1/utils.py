import os
import sys #so we can handle custom exception
from src.ml_project_1.exception import CustomException # import the custom exception
from src.ml_project_1.logger import logging # import the loggeer
import pandas as pd
from dotenv import load_dotenv # load_dotenv will load all variables
import pymysql


load_dotenv() # load all the environment variables  

host = os.getenv("host") # get the host from the environment variable
user = os.getenv("user") # get the user from the environment variable
password = os.getenv("password") # get the password from the environment variable
db = 'college' # use the college database

# utils is for general functionality

def read_sql_data(): # function to read data from sql
    logging.info("Reading from mysql database started") #this is used to capture logs. this will return database
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        ) #connect to the database  
        logging.info("connection established",mydb) # log the database connection
        df=pd.read_sql_query("SELECT * FROM test",mydb) # read the data from the test table
        print(df.head())

        return df # return the data         
          
    except CustomException as e:
        raise CustomException(e,sys)