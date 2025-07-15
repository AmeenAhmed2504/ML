# Import necessary libraries

#Program 7 Write a program to perform House price predict using Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

# Given data sample
data = np.array([
    [1500, 5, 200],
    [1200, 2, 180],
    [1800, 4, 220],
    [1000, 1, 160],
    [1400, 3, 190]
])

# Separate features (size and age) and target (price)
x = data[:, :2]  # Features: size (sq. ft) and age (years)
y = data[:, 2]   # Target: price (in Lakhs)

# Create and train the linear regression model
model = LinearRegression()
model.fit(x, y)  # Corrected: lowercase 'x' (original had 'X')

# Take user inputs for size and age
new_size = float(input("Enter the size of the house (sq. ft): "))
new_age = float(input("Enter the age of the house (years): "))

# Predict the price for the new data point
predicted_price = model.predict([[new_size, new_age]])

# Print the predicted price
print("Predicted Price for a house with size {} sq. ft and age {} years: {:.2f} Lakhs".format(
    new_size, new_age, predicted_price[0]
))
