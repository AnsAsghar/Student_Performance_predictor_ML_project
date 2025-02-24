# Student Performance Predictor using Machine Learning 🚀

## Overview
This project is an end-to-end machine learning pipeline designed to predict student performance. It starts with data ingestion from a MySQL database, followed by thorough preprocessing and standardization of features, and continues with training multiple regression models—Random Forest, XGBoost, and CatBoost—to select the best performer based on the R2 score. Built with production-ready software engineering practices, the project incorporates modular design, proper error handling, logging, and MLflow integration for experiment tracking.

## Key Steps
1. __Data Ingestion:__ Fetch student data from a MySQL database.
2. __Data Transformation:__ Preprocess and standardize features to prepare for modeling.
3. __Model Training:__ Train multiple regression models to predict student performance.
4. __Model Selection:__ Evaluate models based on R2 score and select the best one.
5. __Artifact Generation:__ Save preprocessed data splits, trained model artifacts, and performance metrics for future use.

## Project Structure
- __data_ingestion/__  
  Handles extraction of student data from the MySQL database.

- __data_transformation/__  
  Contains scripts for data cleaning, preprocessing, and standardization.

- __model_training/__  
  Includes modules for training various regression models and selecting the best performer.

- __logging/__  
  Centralizes logging configurations to monitor the execution of the pipeline.

- __mlflow/__  
  Integrates with MLflow for comprehensive experiment tracking and performance logging.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/AnsAsghar/ML-Project-1.git
   ```
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To check the final score and best model
```
python app.py
```
To run the entire pipeline, execute:
```
python run_pipeline.py
```
This command triggers the complete workflow—from data ingestion to model training and artifact generation.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes with clear messages.
4. Open a pull request for review.


## Connect with Me
LinkedIn: [Anas Asghar Linkedn](https://www.linkedin.com/in/anas-asghar-aa7575202/)
YouTube: [My Youtube Channel](https://www.youtube.com/channel/UCejaga6msq18if3kap8m_ew)]  
Instagram: [My instagram account](https://www.instagram.com/ansasghar)]

Happy coding! 😊
