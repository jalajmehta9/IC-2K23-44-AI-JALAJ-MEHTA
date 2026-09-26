import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

print("\nDataset Information:")
print(df.info())