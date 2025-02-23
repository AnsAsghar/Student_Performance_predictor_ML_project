import logging
import sys
from src.ml_project_1.logger import logging
from src.ml_project_1.exception import CustomException
from src.ml_project_1.components.data_ingestion import DataIngestion
from src.ml_project_1.components.data_transformation import DataTransformation

if __name__ == "__main__":
    logging.info("The execution has started")

    try: 
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_path, test_path)
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e, sys)