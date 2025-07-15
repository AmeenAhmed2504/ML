#Program 10 Write a program to implement a linear regression model for regression tasks and Train the model on a dataset with continuous target variables.
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1000, 2], [1500, 3], [1200, 2], [1800, 4], [900, 2], [2000, 3]])
y = np.array([300000, 400000, 350000, 500000, 280000, 450000])
model = LinearRegression()
model.fit(X, y)
size = float(input("enter the size of the house in sqft: "))
bedrooms = int(input("enter the number of bedrooms: "))
new_data = np.array([[size,bedrooms]])
predicted_price = model.predict(new_data)
print("predicted price for a house with size {} sqft and {} bedrooms: Rs.{:.2f}".format(size,bedrooms,predicted_price[0]))
