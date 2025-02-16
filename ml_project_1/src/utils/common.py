def load_data(file_path: str):
    """
    Load data from a specified file path.
    
    Args:
        file_path (str): The path to the data file.
        
    Returns:
        data: Loaded data.
    """
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def save_data(data, file_path: str):
    """
    Save data to a specified file path.
    
    Args:
        data: The data to save.
        file_path (str): The path to save the data file.
    """
    import pandas as pd
    data.to_csv(file_path, index=False)

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and encoding categorical variables.
    
    Args:
        data: The data to preprocess.
        
    Returns:
        data: Preprocessed data.
    """
    # Example preprocessing steps
    data.fillna(method='ffill', inplace=True)  # Fill missing values
    # Add more preprocessing steps as needed
    return data

def split_data(data, target_column: str, test_size: float = 0.2):
    """
    Split the data into training and testing sets.
    
    Args:
        data: The data to split.
        target_column (str): The name of the target column.
        test_size (float): The proportion of the dataset to include in the test split.
        
    Returns:
        X_train, X_test, y_train, y_test: Split data.
    """
    from sklearn.model_selection import train_test_split
    
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    return X_train, X_test, y_train, y_test