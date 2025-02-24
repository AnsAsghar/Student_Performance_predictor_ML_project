#### Student Performance Predictor using Machine Learning

This is a Machine Learning project focused on student performance prediction. The project implements an end-to-end ML pipeline that starts with data ingestion from a MySQL database containing student information, transforms the data through preprocessing steps like standardization, and trains multiple regression models to predict student performance. The pipeline evaluates several models including Random Forest, XGBoost, and CatBoost, selecting the best performer based on R2 score. The project follows software engineering best practices with modular components, proper exception handling, logging, and MLflow integration for experiment tracking. The final output includes trained model artifacts, preprocessed data splits, and performance metrics that can be used for making predictions on new student data. The project structure is organized into clear components (data ingestion, transformation, model training) with proper separation of concerns, making it maintainable and scalable.

## Key steps involved:

1. Data Ingestion: Fetches student data from MySQL database
2. Data Transformation: Preprocesses and standardizes features
3. Model Training: Trains and evaluates multiple regression models
4. Model Selection: Picks the best performing model based on R2 score
5. Artifact Generation: Saves preprocessed data and trained model for future use

   
# The project demonstrates professional software development practices including proper error handling, logging, modular design, and integration with MLflow for experiment tracking, making it production-ready and maintainable
