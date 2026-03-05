import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# database connection
engine = create_engine("postgresql://postgres:postgres123@localhost:5432/salesdb")

# -------------------------
# Queries
# -------------------------

product_query = """
SELECT product, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
"""

region_query = """
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC
"""

category_query = """
SELECT category, SUM(revenue) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC
"""

month_query = """
SELECT month, SUM(revenue) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month
"""

df_product = pd.read_sql(product_query, engine)
df_region = pd.read_sql(region_query, engine)
df_category = pd.read_sql(category_query, engine)
df_month = pd.read_sql(month_query, engine)

# -------------------------
# Create Report
# -------------------------

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Revenue by Product
axes[0,0].bar(df_product["product"], df_product["total_revenue"])
axes[0,0].set_title("Revenue by Product")

# Revenue by Region
axes[0,1].bar(df_region["region"], df_region["total_revenue"])
axes[0,1].set_title("Revenue by Region")

# Category Performance
axes[1,0].bar(df_category["category"], df_category["total_revenue"])
axes[1,0].set_title("Category Performance")

# Monthly Trend
axes[1,1].plot(df_month["month"], df_month["total_revenue"], marker="o")
axes[1,1].set_title("Monthly Revenue Trend")

plt.tight_layout()

plt.savefig("reports/sales_report.png")

print("Sales report generated successfully!")