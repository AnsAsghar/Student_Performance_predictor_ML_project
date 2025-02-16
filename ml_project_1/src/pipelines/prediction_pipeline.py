from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def predict(self, data_path: str):
        # Step 1: Ingest data
        data = self.data_ingestion.ingest_data(data_path)

        # Step 2: Transform data
        transformed_data = self.data_transformation.transform_data(data)

        # Step 3: Make predictions
        predictions = self.model_trainer.predict(transformed_data)

        return predictions

# Example usage:
# if __name__ == "__main__":
#     pipeline = PredictionPipeline()
#     predictions = pipeline.predict("path/to/new/data.csv")
#     print(predictions)