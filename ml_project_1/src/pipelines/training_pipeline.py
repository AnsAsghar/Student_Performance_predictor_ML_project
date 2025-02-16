from src.components.data_ingestion import load_data
from src.components.data_transformation import transform_data
from src.components.model_trainer import train_model

def run_training_pipeline(data_source: str, transformation_params: dict, model_params: dict):
    # Step 1: Data Ingestion
    data = load_data(data_source)
    
    # Step 2: Data Transformation
    transformed_data = transform_data(data, **transformation_params)
    
    # Step 3: Model Training
    model = train_model(transformed_data, **model_params)
    
    return model

if __name__ == "__main__":
    # Example usage
    data_source = "path/to/dataset.csv"
    transformation_params = {"feature_selection": True}
    model_params = {"model_type": "RandomForest", "n_estimators": 100}
    
    trained_model = run_training_pipeline(data_source, transformation_params, model_params)
    print("Model training completed.")