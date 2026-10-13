# MGS 3101 - Assignment 2


import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("../data/Sales-Export_2019-2020.csv")

print("Shape of the data:")
print(df.shape)

print("\nData types:")
print(df.dtypes)

print("\nFirst five rows:")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

df.columns = df.columns.str.strip()

df["order_value_EUR"] = df["order_value_EUR"].str.replace(",", "")
df["order_value_EUR"] = df["order_value_EUR"].astype(float)

df["date"] = pd.to_datetime(df["date"])

df["profit"] = df["order_value_EUR"] - df["cost"]

print("\nOrder value statistics:")
print("Count:", df["order_value_EUR"].count())
print("Mean:", df["order_value_EUR"].mean())
print("Median:", df["order_value_EUR"].median())
print("Min:", df["order_value_EUR"].min())
print("Max:", df["order_value_EUR"].max())
print("Standard deviation:", df["order_value_EUR"].std())

print("\nCost statistics:")
print("Count:", df["cost"].count())
print("Mean:", df["cost"].mean())
print("Median:", df["cost"].median())
print("Min:", df["cost"].min())
print("Max:", df["cost"].max())
print("Standard deviation:", df["cost"].std())

print("\nTotal revenue by country:")
country_revenue = df.groupby("country")["order_value_EUR"].sum()
print(country_revenue.sort_values(ascending=False))

print("\nAverage order value by country:")
country_average = df.groupby("country")["order_value_EUR"].mean()
print(country_average.sort_values(ascending=False))

print("\nHighest order:")
highest = df["order_value_EUR"].max()
print(df[df["order_value_EUR"] == highest])

print("\nLowest order:")
lowest = df["order_value_EUR"].min()
print(df[df["order_value_EUR"] == lowest])

total_revenue = df["order_value_EUR"].sum()
total_profit = df["profit"].sum()
margin = total_profit / total_revenue * 100

print("\nProfit margin check:")
print("Profit margin is", round(margin, 1), "%")

if margin >= 15:
    print("The profit margin meets the 15% goal.")
else:
    print("The profit margin is below the 15% goal.")


# Recommendation 1: Top customers
print("\nTop 5 customers by revenue:")
customer_revenue = df.groupby("customer_name")["order_value_EUR"].sum()
customer_revenue = customer_revenue.sort_values(ascending=False)
print(customer_revenue.head(5))
customer_revenue.to_csv("rec1_revenue_by_customer.csv")

# Recommendation 2: Number of orders by country
print("\nNumber of orders by country:")
country_orders = df.groupby("country")["order_id"].count()
print(country_orders.sort_values(ascending=False))
country_average.to_csv("rec2_countries.csv")

# Recommendation 3: Revenue by month
print("\nRevenue by month (1 = January, 12 = December):")
df["month"] = df["date"].dt.month
month_revenue = df.groupby("month")["order_value_EUR"].sum()
print(month_revenue)
month_revenue.to_csv("rec3_revenue_by_month.csv")

# Recommendation 4: Average order value by device
print("\nAverage order value by device:")
device_average = df.groupby("device_type")["order_value_EUR"].mean()
print(device_average)
device_average.to_csv("rec4_device_type.csv")

# Step 13: Summary
print("\nSummary of findings:")
print("- The data has 1,000 orders and no missing values.")
print("- The profit margin is about 16.8%, which meets my 15% goal.")
print("- Portugal, France and Sweden bring in the most revenue.")
print("- Johns and Sons is the biggest customer by far.")
print("- June and December are the busiest months. February is the slowest.")
print("- PC orders have a higher average order value than mobile orders.")