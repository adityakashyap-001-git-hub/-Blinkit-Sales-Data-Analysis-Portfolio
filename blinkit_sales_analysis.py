
# Blinkit Sales Data Analysis
# Author: Aditya Kashyap
# Description: Data cleaning and analysis for Blinkit grocery sales dataset

import pandas as pd
import numpy as np

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("blinkit_sales.csv")

# -----------------------------
# Data Cleaning
# -----------------------------

# Remove missing Order IDs, Sales, Profit
df.dropna(subset=['Order ID', 'Sales', 'Profit'], inplace=True)

# Convert Delivery Time to numeric
df['Delivery Time'] = pd.to_numeric(df['Delivery Time'])

# Remove duplicates
df.drop_duplicates(inplace=True)

print("Data after cleaning:")
print(df.head())

# -----------------------------
# Data Analysis
# -----------------------------

# Category-wise Revenue
category_revenue = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nCategory-wise Revenue:")
print(category_revenue)

# Profit by Product
product_profit = df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Product:")
print(product_profit)

# Orders by City
orders_city = df['City'].value_counts()
print("\nOrders by City:")
print(orders_city)

# Average Delivery Time
avg_delivery_time = df['Delivery Time'].mean()
print("\nAverage Delivery Time:", avg_delivery_time)

# -----------------------------
# Key Metrics
# -----------------------------

total_revenue = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()

print("\nKey Metrics")
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv("cleaned_blinkit_sales.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_blinkit_sales.csv'")
