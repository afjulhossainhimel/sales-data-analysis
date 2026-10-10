import pandas as pd
import matplotlib.pyplot as plt


# ==============================
# 1. Load Dataset
# ==============================

df = pd.read_csv("sales_data_analysis.csv")


# ==============================
# 2. Data Preparation
# ==============================

df["Date"] = pd.to_datetime(df["Date"])


# ==============================
# 3. Basic Data Inspection
# ==============================

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# ==============================
# 4. Sales Analysis
# ==============================

total_sales = df["Total_Sales"].sum()

print("\nTotal Sales:")
print(f"৳{total_sales:,.0f}")


product_sales = df.groupby("Product")["Total_Sales"].sum()

print("\nSales by Product:")
print(product_sales)


category_sales = df.groupby("Category")["Total_Sales"].sum()

print("\nSales by Category:")
print(category_sales)


quantity_by_product = df.groupby("Product")["Quantity"].sum()

print("\nQuantity Sold by Product:")
print(quantity_by_product)


monthly_sales = df.groupby(
    df["Date"].dt.to_period("M")
)["Total_Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)


# ==============================
# 5. Additional Business Metrics
# ==============================

average_order_value = df["Total_Sales"].mean()

print("\nAverage Order Value:")
print(f"৳{average_order_value:,.2f}")


best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

print("\nTop Revenue Product:")
print(f"{best_product} - ৳{best_product_sales:,.0f}")


average_price = df.groupby("Product")["Unit_Price"].mean()

print("\nAverage Unit Price by Product:")
print(average_price)


product_sales_percentage = (
    product_sales / total_sales
) * 100

print("\nSales Contribution by Product (%):")
print(product_sales_percentage.round(2))


# ==============================
# 6. Visualizations
# ==============================

# Monthly Sales Chart

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()


# Sales Contribution by Product Chart

product_sales_percentage.plot(kind="bar")

plt.title("Sales Contribution by Product")
plt.xlabel("Product")
plt.ylabel("Sales Contribution (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("sales_contribution_by_product.png")
plt.show()


# Sales by Product Chart

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()