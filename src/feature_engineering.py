import pandas as pd


def standardize_fat_content(df):
    """
    Fix inconsistent labels in Item_Fat_Content
    """

    df["Item_Fat_Content"] = df["Item_Fat_Content"].replace({
        "LF": "Low Fat",
        "low fat": "Low Fat",
        "reg": "Regular"
    })

    return df


def create_outlet_age(df):
    """
    Create Outlet_Age feature
    """

    current_year = 2025
    df["Outlet_Age"] = current_year - df["Outlet_Establishment_Year"]

    return df


def log_transform_sales(df):
    """
    Optional transformation for skewed target variable
    """

    df["Item_Outlet_Sales_Log"] = df["Item_Outlet_Sales"].apply(lambda x: x)

    return df