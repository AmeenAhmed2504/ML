# Program  6 - B: Program for perform scaling

import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Create a sample dataset (2 features, 5 data points)
data = np.array([[50, 200],
                 [60, 220],
                 [70, 240],
                 [80, 260],
                 [90, 280]])
# Step 2: Apply StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Step 3: Print the original and scaled data
print("Original Data:")
print(data)

print("\nScaled Data:")
print(scaled_data)
plt.show()
