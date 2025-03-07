import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.ml_project_1.utils import save_object
from src.ml_project_1.exception import CustomException
from src.ml_project_1.logger import logging

import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["feature1", "feature2"]

            num_pipeline = Pipeline(
                steps=[
                    ("std_scaler", StandardScaler()),
                ]
            )

            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_columns),
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading the train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "target"
            numerical_columns = ["feature1", "feature2"]

            input_features_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_features_train_df = train_df[target_column_name]

            input_features_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_features_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing datasets")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_features_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_features_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_features_test_df)]

            logging.info("Saving preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
        