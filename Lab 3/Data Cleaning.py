import pandas as pd

df = pd.read_csv("data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where all values are missing
df = df.dropna(how="all")

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Convert string columns by removing extra spaces
for column in df.select_dtypes(include="object"):
    df[column] = df[column].str.strip()

print("Cleaned Dataset:")
print(df.head())

print("\nShape after cleaning:")
print(df.shape)