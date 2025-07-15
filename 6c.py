#Program 6 c) Write a Program to perform Categorical encoding

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red'], 'Size': ['S', 'M', 'L', 'M', 'S']}
df = pd.DataFrame(data)

# Label Encoding for 'Color' column
df['Color_Encoded'] = LabelEncoder().fit_transform(df['Color'])

# One-Hot Encoding for 'Size' column
df = pd.get_dummies(df, columns=['Size'], drop_first=True)

# Output the result
print(df)
