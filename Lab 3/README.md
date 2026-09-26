# Data Loading, Cleaning, and Exploratory Data Analysis

This repository contains three Python scripts that demonstrate basic data preparation and exploratory data analysis (EDA) using the **Pandas** library. Each script reads a dataset named `data.csv` and performs a different stage of a simple data analysis workflow.

## Project Contents

| File | Purpose |
|---|---|
| `Dataset Loading.py` | Loads `data.csv` and displays its first five rows and dataset information. |
| `Data Cleaning.py` | Removes duplicate rows and fully empty rows, and trims extra spaces from column names and string values. |
| `Exploratory Data Analysis.py` | Examines the dataset's rows, dimensions, columns, data types, descriptive statistics, unique values, and missing values. |

## Requirements

- Python 3.x
- Pandas

Install Pandas using:

```bash
pip install pandas
```

## Dataset

All three scripts expect a CSV file named:

```text
data.csv
```

Place `data.csv` in the working directory from which you run the scripts. The uploaded Python files do not include the dataset itself, so you must provide your own `data.csv`.

## How to Run

Open a terminal in the project directory and run the scripts individually:

```bash
python "Dataset Loading.py"
python "Data Cleaning.py"
python "Exploratory Data Analysis.py"
```

On systems where Python 3 is invoked using `python3`, replace `python` with `python3`.

---

## 1. Dataset Loading

**File:** `Dataset Loading.py`

### Purpose

This script loads the CSV dataset into a Pandas DataFrame and displays a quick preview and information about the dataset.

### How It Works

1. Imports the Pandas library.
2. Reads `data.csv` using `pd.read_csv()`.
3. Displays the first five rows using `df.head()`.
4. Displays dataset information using `df.info()`.

### Key Pandas Functions

| Function | Description |
|---|---|
| `pd.read_csv("data.csv")` | Reads the CSV file into a DataFrame. |
| `df.head()` | Displays the first five rows by default. |
| `df.info()` | Displays information such as column names, non-null counts, and data types. |

---

## 2. Data Cleaning

**File:** `Data Cleaning.py`

### Purpose

This script performs basic cleaning operations on the dataset after loading `data.csv`.

### Cleaning Operations

1. **Remove duplicate rows:** `df.drop_duplicates()` removes duplicate records.
2. **Remove fully empty rows:** `df.dropna(how="all")` removes rows in which every value is missing.
3. **Trim column names:** `df.columns.str.strip()` removes leading and trailing spaces from column names.
4. **Trim string values:** The script selects columns with the `object` data type and applies `.str.strip()` to remove leading and trailing spaces from their string values.

### Output

The script displays:

- The first five rows of the cleaned DataFrame using `df.head()`.
- The shape of the cleaned dataset using `df.shape`, showing the number of rows and columns after cleaning.

### Important Note

The script removes rows only when all their values are missing. It does not remove rows that contain some missing values, fill missing values, or convert column data types.

---

## 3. Exploratory Data Analysis (EDA)

**File:** `Exploratory Data Analysis.py`

### Purpose

This script performs an initial examination of the dataset to understand its structure, contents, and basic statistical properties.

### Analysis Performed

| Operation | Pandas Expression | What It Shows |
|---|---|---|
| First five rows | `df.head()` | First five records. |
| Last five rows | `df.tail()` | Last five records. |
| Dataset shape | `df.shape` | Number of rows and columns. |
| Column names | `df.columns` | Names of all columns. |
| Data types | `df.dtypes` | Data type of each column. |
| Statistical summary | `df.describe()` | Descriptive statistics for applicable columns. |
| Unique values | `df.nunique()` | Number of distinct values in each column. |
| Missing values | `df.isnull().sum()` | Number of missing values in each column. |

The script prints the result of each operation to the terminal.

---

## Suggested Workflow

The three scripts represent common stages of a basic data analysis process:

1. **Load the dataset** using `Dataset Loading.py` to inspect its initial contents and structure.
2. **Clean the dataset** using `Data Cleaning.py` to remove duplicates, fully empty rows, and unwanted surrounding spaces.
3. **Explore the dataset** using `Exploratory Data Analysis.py` to inspect its dimensions, columns, data types, statistics, unique values, and missing values.

**Note:** Each script independently reads the original file named `data.csv`. The cleaning script does not save the cleaned DataFrame to a new CSV file. Therefore, running the EDA script afterward will analyze the original CSV unless you separately save and load the cleaned data.

## Concepts Demonstrated

- Reading CSV files with Pandas.
- Working with Pandas DataFrames.
- Previewing and inspecting datasets.
- Checking dataset dimensions and column data types.
- Removing duplicate records.
- Removing fully empty rows.
- Cleaning whitespace in column names and string values.
- Generating descriptive statistics.
- Counting unique and missing values.
- Performing basic exploratory data analysis.

## Conclusion

These scripts demonstrate a simple data analysis workflow using Python and Pandas. They cover loading a CSV dataset, performing basic cleaning operations, and exploring the dataset to understand its structure and quality.
