import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = None

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the data by handling missing values and converting data types if necessary.
        """
        df = df.dropna()  # Drop missing values for simplicity
        # Additional data cleaning steps can be added here
        return df

    def normalize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalizes the data to a range [0, 1] using Min-Max scaling.
        """
        self.scaler = MinMaxScaler()
        normalized_data = self.scaler.fit_transform(df)
        return pd.DataFrame(normalized_data, columns=df.columns)

    def standardize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardizes the data to have a mean of 0 and a standard deviation of 1.
        """
        self.scaler = StandardScaler()
        standardized_data = self.scaler.fit_transform(df)
        return pd.DataFrame(standardized_data, columns=df.columns)

# Example usage
if __name__ == "__main__":
    df = pd.DataFrame({
        'A': [1, 2, 3, np.nan, 5],
        'B': [5, 4, np.nan, 2, 1]
    })

    preprocessor = DataPreprocessor()
    cleaned_data = preprocessor.clean_data(df)
    normalized_data = preprocessor.normalize_data(cleaned_data)
    standardized_data = preprocessor.standardize_data(cleaned_data)

    print(f"Cleaned Data:\n{cleaned_data}\n")
    print(f"Normalized Data:\n{normalized_data}\n")
    print(f"Standardized Data:\n{standardized_data}\n")