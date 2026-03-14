Big Mart Sales Prediction
📌 Project Overview

This project analyzes retail sales data from Big Mart stores to understand the factors affecting product sales and build a predictive model for Item_Outlet_Sales.

The dataset contains sales information for 1,559 products across 10 stores in different cities, with a total of 8,523 observations and 12 features.

The goal of this project is to perform Exploratory Data Analysis (EDA), data preprocessing, and machine learning modeling to predict sales and gain insights that can help improve inventory and pricing strategies.

📊 Dataset Information
Attribute	Description
Item_Identifier	Unique ID for each product
Item_Weight	Weight of the product
Item_Fat_Content	Fat content category
Item_Visibility	Percentage of display area allocated
Item_Type	Category of product
Item_MRP	Maximum Retail Price
Outlet_Identifier	Unique store ID
Outlet_Establishment_Year	Year the outlet was established
Outlet_Size	Store size
Outlet_Location_Type	City tier
Outlet_Type	Type of store
Item_Outlet_Sales	Sales of product in a store (Target Variable)

🧹 Data Preprocessing

The preprocessing pipeline includes:

Checking missing values

Handling missing data:

Item_Weight → Mean imputation

Outlet_Size → Mode imputation

Handling zero values in Item_Visibility

Preparing dataset for feature engineering and modeling

🧹 Data Cleaning

Two columns had missing values:

Column	Missing %
Item_Weight	17.16%
Outlet_Size	28.27%

Handling strategy:

Item_Weight → filled with mean

Outlet_Size → filled with mode