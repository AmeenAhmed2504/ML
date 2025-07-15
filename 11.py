# Program 11Write a program to implement a decision tree classifier using scikit-learn and visualize the decision tree and understand its splits.
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np
# Create a simple dataset (8 samples, 2 features)
# Features: [Temperature, Humidity]
X = np.array([
    [30, 70],  # Sample 1
    [22, 60],  # Sample 2
    [28, 65],  # Sample 3
    [35, 55],  # Sample 4
    [20, 80],  # Sample 5
    [25, 75],  # Sample 6
    [33, 50],  # Sample 7
    [31, 55]   # Sample 8
])
# Labels (0 = No Rain, 1 = Rain)
y = np.array([1, 1, 0, 0, 1, 1, 0, 0])
# Train Decision Tree
clf = DecisionTreeClassifier()
clf.fit(X, y)
# Visualize Decision Tree
plt.figure(figsize=(10, 6))
plot_tree(clf, filled=True, feature_names=["Temperature", "Humidity"], class_names=["No Rain", "Rain"])
plt.title("Decision Tree on Weather Data")
plt.show()
