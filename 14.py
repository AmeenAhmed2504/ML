# Program 14 Write a Program to handle outliers
import numpy as np
from scipy.stats import zscore

# Data with outliers
data = np.random.normal(50, 10, 100).tolist() + [150, 200, 300]

# Calculate Z-scores and detect outliers (Z > 3 or Z < -3)
outliers = np.abs(zscore(data)) > 3

# Print outliers
print("Outliers:", np.array(data)[outliers])
