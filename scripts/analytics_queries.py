import pandas as pd
from sqlalchemy import create_engine

# database connection
engine = create_engine("postgresql://postgres:postgres123@localhost:5432/salesdb")

# 1️⃣ Top selling products
query1 = """
SELECT product, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;
"""

top_products = pd.read_sql(query1, engine)
print("\nTop Selling Products")
print(top_products)


# 2️⃣ Revenue by region
query2 = """
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;
"""

region_sales = pd.read_sql(query2, engine)
print("\nRevenue by Region")
print(region_sales)


# 3️⃣ Category performance
query3 = """
SELECT category, SUM(revenue) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;
"""

category_sales = pd.read_sql(query3, engine)
print("\nCategory Performance")
print(category_sales)


# 4️⃣ Monthly trend
query4 = """
SELECT month, SUM(revenue) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month;
"""

monthly_sales = pd.read_sql(query4, engine)
print("\nMonthly Revenue Trend")
print(monthly_sales)