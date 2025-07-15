import pandas as pd

# Define the file paths
csv_file_path = 'C:\ML_Projects\sample_data.csv'
excel_file_path = 'C:\ML_Projects\sample_data.xlsx'

# Load the CSV file
data_csv = pd.read_csv(csv_file_path)
print("CSV File Data:")
print(data_csv)

# Load the Excel file
data_excel = pd.read_excel(excel_file_path)
print("\nExcel File Data:")
print(data_excel)

# Basic Data Exploration
print("\nData Descriptions:")
print("CSV Data Description:")
print(data_csv.describe())

print("\nExcel Data Description:")
print(data_excel.describe())
 #Displaying data types
print("\nDATA types in csv file:")
print(data_csv.dtypes)

print("\n print data types in excel file:")
print(data_excel.dtypes)
