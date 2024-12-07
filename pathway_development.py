import os
import json
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sympy import symbols, Eq, solve
from typing import List, Dict, Any

class PathwayDevelopment:
    def __init__(self, dataset_dir: str = "output", learning_dataset: str = "learning_data.csv"):
        """
        Initializes the PathwayDevelopment class for analyzing, evaluating, and creating pathways.
        
        :param dataset_dir: Directory containing datasets fetched by `baby_steps.py`.
        :param learning_dataset: Path to the file where the system's learning data is stored.
        """
        self.dataset_dir = dataset_dir
        self.learning_dataset = learning_dataset
        self.dataframes = []
        self.pathways = []
        self._load_datasets()

    def _load_datasets(self) -> None:
        """
        Loads datasets from the specified directory into memory as Pandas DataFrames.
        """
        print("Loading datasets for analysis...")
        for file_name in os.listdir(self.dataset_dir):
            file_path = os.path.join(self.dataset_dir, file_name)
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)
                if isinstance(data, list):
                    df = pd.DataFrame(data)
                elif isinstance(data, dict):
                    df = pd.DataFrame([data])
                else:
                    print(f"Unknown data format in {file_name}")
                    continue
                self.dataframes.append(df)
                print(f"Loaded {file_name}")
            except Exception as e:
                print(f"Error loading {file_name}: {e}")

    def analyze_and_evaluate(self) -> None:
        """
        Analyzes and evaluates datasets to identify key insights for pathway development.
        """
        print("Analyzing and evaluating datasets...")
        for df in self.dataframes:
            try:
                # Standardize the data
                scaler = StandardScaler()
                standardized_data = scaler.fit_transform(df.select_dtypes(include=[np.number]))
                
                # Apply clustering to find groupings
                kmeans = KMeans(n_clusters=3, random_state=42)
                labels = kmeans.fit_predict(standardized_data)
                df['Cluster'] = labels
                print(f"Clusters identified:\n{df['Cluster'].value_counts()}")
                
                # Extract patterns and relationships
                for col in df.select_dtypes(include=[np.number]).columns:
                    mean_value = df.groupby('Cluster')[col].mean()
                    print(f"Mean {col} by cluster:\n{mean_value}")
                
                # Add processed data to learning dataset
                self._add_to_learning_data(df)
            except Exception as e:
                print(f"Error analyzing dataset: {e}")

    def _add_to_learning_data(self, df: pd.DataFrame) -> None:
        """
        Adds analyzed data to the learning dataset for system training.
        
        :param df: DataFrame to append to the learning dataset.
        """
        if not os.path.exists(self.learning_dataset):
            df.to_csv(self.learning_dataset, index=False)
            print(f"Created learning dataset: {self.learning_dataset}")
        else:
            existing_data = pd.read_csv(self.learning_dataset)
            combined_data = pd.concat([existing_data, df], ignore_index=True)
            combined_data.to_csv(self.learning_dataset, index=False)
            print(f"Updated learning dataset: {self.learning_dataset}")

    def create_pathways(self) -> None:
        """
        Creates mathematical pathways (formulas) based on data relationships.
        """
        print("Creating pathways from data relationships...")
        x, y, z = symbols('x y z')
        
        for df in self.dataframes:
            try:
                if len(df.select_dtypes(include=[np.number]).columns) < 2:
                    print("Insufficient numeric columns for pathway creation.")
                    continue
                
                # Example: Fit a linear relationship between first two numeric columns
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                col1, col2 = numeric_cols[:2]
                coeff = np.polyfit(df[col1], df[col2], 1)
                equation = Eq(y, coeff[0] * x + coeff[1])
                self.pathways.append(equation)
                print(f"Created pathway: {equation}")
            except Exception as e:
                print(f"Error creating pathways: {e}")

    def save_pathways(self, output_file: str = "pathways.txt") -> None:
        """
        Saves created pathways to a text file.
        
        :param output_file: Path to the file where pathways are saved.
        """
        try:
            with open(output_file, "w") as f:
                for pathway in self.pathways:
                    f.write(str(pathway) + "\n")
            print(f"Saved pathways to {output_file}")
        except Exception as e:
            print(f"Error saving pathways: {e}")

# Example usage
if __name__ == "__main__":
    pathway_dev = PathwayDevelopment()
    pathway_dev.analyze_and_evaluate()
    pathway_dev.create_pathways()
    pathway_dev.save_pathways()