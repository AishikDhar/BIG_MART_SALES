
import pandas as pd
from src.data_cleaning import check_missing_values, handle_missing_values


# Load dataset
df = pd.read_csv("big_mart_sales.csv")

# Check missing values
missing = check_missing_values(df)
print("Missing Values:\n", missing)

# Handle missing values
df = handle_missing_values(df)

# Verify again
print("\nAfter Cleaning:\n", df.isnull().sum())