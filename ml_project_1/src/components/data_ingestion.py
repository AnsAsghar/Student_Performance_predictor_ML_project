from typing import Any, Dict
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)

def ingest_data(source: str, **kwargs: Any) -> pd.DataFrame:
    """
    Ingest data from various sources.

    Parameters:
    source (str): The source of the data (e.g., 'csv', 'json').
    **kwargs: Additional arguments for specific data sources.

    Returns:
    pd.DataFrame: DataFrame containing the ingested data.
    """
    if source == 'csv':
        return load_data(kwargs.get('file_path'))
    elif source == 'json':
        return pd.read_json(kwargs.get('file_path'))
    else:
        raise ValueError(f"Unsupported data source: {source}")