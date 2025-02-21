import os
import pandas as pd
from sqlalchemy import create_engine
from src.ml_project_1.utils.database import get_db_connection
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.ml_project_1.logger import logging
from src.ml_project_1.exception import CustomException
import sys

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Initiating data ingestion process")
            
            # Use sample data instead of MySQL database
            df = pd.DataFrame({
                'feature1': range(100),
                'feature2': range(100, 200),
                'target': [i % 2 for i in range(100)]
            })
            logging.info(f"Created sample dataset with {len(df)} rows")
            
            # Create artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(f"Raw data saved to {self.ingestion_config.raw_data_path}")
            
            # Split the data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            # Save train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Train-test split completed and saved")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            logging.error(f"Error in data ingestion: {str(e)}")
            raise CustomException(e, sys)
        