#Program 8.Write a program to Binary Classification using Logistic Regression
import numpy as np
from sklearn.linear_model import LogisticRegression

# Binary Classification Example
# Data for binary classification (hours studied and pass/fail)
x_binary = np.array([[2], [4], [6], [8], [10]])  # Hours studied
y_binary = np.array([0, 0, 1, 1, 1])  # Pass (1) or Fail (0)

# Train a Logistic Regression model for binary classification
model_binary = LogisticRegression()
model_binary.fit(x_binary, y_binary)

# User input for prediction
hours_studied = float(input("Enter the number of hours studied: "))

# Predictions
binary_prediction = model_binary.predict_proba([[hours_studied]])

# Output
if binary_prediction[0][1] >= 0.5:
    print("Binary Classification - Predicted class: PASS")
else:
    print("Binary Classification - Predicted class: FAIL")
