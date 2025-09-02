import pandas as pd
import requests
from io import StringIO

# URL of the CSV file
url = "https://raw.githubusercontent.com/izzanwafiy26-code/wafiy/refs/heads/main/Finance_data.csv"

try:
    # Read the CSV file directly from the URL
    df = pd.read_csv(url)
    
    print("File successfully loaded!")
    print(f"Shape of the dataset: {df.shape}")
    print("\nFirst few rows of the data:")
    print(df.head())
    
    print("\nColumn names:")
    print(df.columns.tolist())
    
    print("\nBasic information about the dataset:")
    print(df.info())
    
    print("\nSummary statistics:")
    print(df.describe())
    
except Exception as e:
    print(f"Error reading the file: {e}")
