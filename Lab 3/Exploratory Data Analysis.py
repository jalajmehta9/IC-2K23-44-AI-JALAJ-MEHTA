import pandas as pd

df = pd.read_csv("data.csv")

# First 5 rows
print("First 5 rows:")
print(df.head())

# Last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Number of rows and columns
print("\nShape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Unique values
print("\nUnique Values:")
print(df.nunique())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())