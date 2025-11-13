import pandas as pd
import os

def load_dataset():
    # Adjust path if CSV is in main project folder
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'dumroo_dataset.csv')
    df = pd.read_csv(csv_path)
    return df
