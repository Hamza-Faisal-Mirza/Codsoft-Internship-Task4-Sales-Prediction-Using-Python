# -*- coding: utf-8 -*-
"""Codsoft-Task4-SALES PREDICTION USING PYTHON.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gpnxKrGpPiNQJSjY3O8PqQZ1EdiSg1Ys
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load and Preprocess the Data
data = pd.read_csv('car_purchasing.csv', encoding='latin1')

# Step 2: Select Features and Target Variable
features = ['age', 'annual Salary', 'credit card debt', 'net worth']
target = 'car purchase amount'

X = data[features]
y = data[target]

# Step 3: Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Choose a Machine Learning Model (Linear Regression)
model = LinearRegression()

# Step 5: Train the Model
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the Model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Sales Predictions for Sample Data
sample_data = [
    [42, 60000, 10000, 250000],
    [41, 65000, 8000, 300000]
]
sample_predictions = model.predict(sample_data)

# Report
report = f"""
------------------------------
Sales Prediction Project Report
------------------------------

Objective:
To forecast future car purchases based on customer data.

1. Data Collection and Preprocessing:
   - Loaded and preprocessed customer data from 'car_purchasing.csv'.

2. Feature Selection:
   - Selected features: {features}
   - Target variable: {target}

3. Machine Learning Model Selection:
   - Chose a Linear Regression model for sales prediction.

4. Model Training and Evaluation:
   - Model trained on customer data.
   - Model performance metrics:
     - Mean Absolute Error (MAE): {mae}
     - Mean Squared Error (MSE): {mse}
     - R-squared (R2): {r2}

5. Predictions for Sample Data:
   - Predicted car purchase amounts for sample data:
     - Data 1: ${sample_predictions[0]:,.2f}
     - Data 2: ${sample_predictions[1]:,.2f}

------------------------------
End of Sales Prediction Report
------------------------------
"""

print(report)