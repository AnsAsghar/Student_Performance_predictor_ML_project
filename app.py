import logging
import sys
from src.ml_project_1.logger import logging
from src.ml_project_1.exception import CustomException
from src.ml_project_1.components.data_ingestion import DataIngestion
from src.ml_project_1.components.data_transformation import DataTransformation
from src.ml_project_1.components.model_trainer import ModelTrainer
from src.ml_project_1.utils import save_object
import mlflow
from urllib.parse import urlparse

if __name__ == "__main__":
    logging.info("The execution has started")
    try:
        # Data ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully")
        
        # Data transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        logging.info("Data transformation completed successfully")
      
        # Model training
        model_trainer = ModelTrainer()
        best_model_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        logging.info(f"Model training completed with best score: {best_model_score}")
        
        # Print the model score
        print(f"Best model score: {best_model_score}")
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise CustomException(e, sys)