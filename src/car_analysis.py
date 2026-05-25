from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Connect to PostgreSQL
engine = create_engine("postgresql://postgres:newpassword123@localhost:5432/carsales_db1")

# Load data
df = pd.read_sql("SELECT * FROM car_sales", engine)

# Create revenue column
df['revenue'] = df['sale_price'] * df['quantity_sold']

# -----------------------------
# 📊 BASIC STATS
# -----------------------------
print("Total Revenue:", df['revenue'].sum())
print("Total Profit:", df['profit'].sum())

# -----------------------------
# 📈 MONTHLY TREND
# -----------------------------
df['sale_date'] = pd.to_datetime(df['sale_date'])

monthly = df.groupby(df['sale_date'].dt.to_period('M'))['revenue'].sum()

print("\nMonthly Revenue:\n", monthly)

# -----------------------------
# 🚗 TOP BRANDS
# -----------------------------
top_brands = df.groupby('brand')['quantity_sold'].sum().sort_values(ascending=False)

print("\nTop Brands:\n", top_brands)

# -----------------------------
# 📊 GRAPH
# -----------------------------
monthly.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

monthly.to_csv("monthly_revenue.csv")

print("\nTop 5 Brands:\n", top_brands.head())
