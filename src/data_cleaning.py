import pandas as pd

def check_missing_values(df):
    """
    Returns missing value count and percentage for each column
    """
    
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100

    missing_df = pd.DataFrame({
        "Missing_Count": missing_count,
        "Missing_Percentage": missing_percent
    })

    return missing_df


def handle_missing_values(df):
    """
    Fill missing values based on column type
    """

    # Numeric column → fill with mean
    if "Item_Weight" in df.columns:
        df["Item_Weight"] = df["Item_Weight"].fillna(df["Item_Weight"].mean())

    # Categorical column → fill with mode
    if "Outlet_Size" in df.columns:
        df["Outlet_Size"] = df["Outlet_Size"].fillna(df["Outlet_Size"].mode()[0])

    return df