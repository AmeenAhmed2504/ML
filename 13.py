# Program 13 Write a program to show matching z score Values
import numpy as np

# Sample data
data = [50, 60, 70, 80, 90, 100]

# Calculate Z-scores
mean = np.mean(data)
std_dev = np.std(data)
z_scores = [(x - mean) / std_dev for x in data]

# Input Z-score to match
input_z = float(input("Enter the Z-score to match: "))

# Find closest matching Z-score
closest_z_index = np.argmin(np.abs(np.array(z_scores) - input_z))
matching_value = data[closest_z_index]

# Output the result
print(f"Data point with Z-score closest to {input_z}: {matching_value}")
