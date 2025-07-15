# Program 5 Write a program to Visualize the dataset to gain insights using Matplotlib or Seaborn by plotting scatter plots, and bar charts.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Step 1: Create a synthetic dataset
np.random.seed(42)
# Generate marks data
math_marks = np.random.randint(50, 90, 100)  # Math marks (50 to 90)
science_marks = np.random.randint(50, 90, 100)  # Science marks (50 to 90)
grades = np.random.choice(['Pass', 'Fail'], size=100, p=[0.7, 0.3])  # Grades: Pass/Fail

# Combine into a DataFrame for better visualization
data = pd.DataFrame({
    'Math': math_marks,
    'Science': science_marks,
    'Grade': grades
})
# Step 2: Scatter plot to show the relationship between Math and Science marks
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Math', y='Science', hue='Grade', data=data, palette='Set1')
plt.title('Scatter Plot: Math vs Science Marks')
plt.xlabel('Math Marks')
plt.ylabel('Science Marks')
plt.show()
# Step 3: Bar chart to visualize the distribution of grades (Pass/Fail)
plt.figure(figsize=(8, 6))
sns.countplot(x='Grade', data=data, palette='Set2')
plt.title('Bar Chart: Pass vs Fail')
plt.xlabel('Grade')
plt.ylabel('Count')
plt.show()
