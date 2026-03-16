
import pandas as pd
from src.data_cleaning import check_missing_values, handle_missing_values
from src.feature_engineering import standardize_fat_content, create_outlet_age


# Load dataset
df = pd.read_csv("big_mart_sales.csv")

# Check missing values
missing = check_missing_values(df)
print("Missing Values:\n", missing)

# Handle missing values
df = handle_missing_values(df)

# Feature engineering
df = standardize_fat_content(df)
df = create_outlet_age(df)

# Verify again
print("\nAfter Cleaning:\n", df.isnull().sum())

print("\nDataset After Feature Engineering:\n")
print(df.head())