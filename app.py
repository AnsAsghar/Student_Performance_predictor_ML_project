import logging
import sys
from src.ml_project_1.logger import logger
from src.ml_project_1.exception import CustomException
from src.ml_project_1.components.data_ingestion import DataIngestion
from src.ml_project_1.components.data_ingestion import DataIngestionConfig


if __name__ == "__main__":
    logging.info("The execution has started")

    try: 
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        


    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e, sys)