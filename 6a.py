# Program 6 Write a program to Handle missing data, encode categorical variables, and perform feature scaling.
import pandas as pd
from sklearn.impute import SimpleImputer
data  = {'Feature1': [10, 20, 30, None, 50],
            'Feature2': [5, None, 15, 20, 25]}
df = pd.DataFrame(data)
imputer = SimpleImputer(strategy="mean") 
df_filled = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print("Original DataFrame with Missing Values:")
print(df)
print("\nDataFrame after Handling Missing Values:")
print(df_filled)
