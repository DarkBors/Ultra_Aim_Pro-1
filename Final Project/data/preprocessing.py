# preprocessing.py
# This file contains functions for data cleaning, scaling, and splitting.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

def calculate_reliability(row, t=87660 * 10):
    lambda_ = 1 / row['ttf']
    return np.exp(-lambda_ * t) * 100

def preprocess_data(file_path):
    # Load the data
    data = pd.read_excel(file_path)

    # Check if columns have the correct data type
    columns_to_check = ['V', 'f', 'T', 'N', 'ttf']
    for col in columns_to_check:
        if not pd.api.types.is_numeric_dtype(data[col]):
            print(f'Column {col} is not numeric.')
            data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with any NaN values
    data = data.dropna()

    # Add a new column for the reliability
    data['reliability'] = data.apply(calculate_reliability, axis=1)

    # Feature Engineering: Add new feature if possible, for now just square of 'N'
    data['N_squared'] = data['N'] ** 2

    # Extract features and targets
    X = data[['V', 'f', 'T', 'N', 'N_squared']].values
    Y_reliability = data['reliability'].values

    # Normalize the inputs
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y_reliability, test_size=0.05, random_state=250)
    
    return X_train, X_test, y_train, y_test, scaler
