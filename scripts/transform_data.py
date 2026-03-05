import pandas as pd
import os

# Get script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Dataset path
file_path = os.path.join(current_dir, "..", "data", "raw_sales_data.csv")

# Load dataset
df = pd.read_csv(file_path)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

print("\n===== ORIGINAL DATA =====")
print(df.head())

# -----------------------------
# 1️⃣ Create Revenue Column
# -----------------------------

df["revenue"] = df["quantity"] * df["price"]

# -----------------------------
# 2️⃣ Extract Month
# -----------------------------

df["month"] = df["date"].dt.month

# -----------------------------
# 3️⃣ Extract Day of Week
# -----------------------------

df["day_of_week"] = df["date"].dt.day_name()

print("\n===== TRANSFORMED DATA =====")
print(df.head())

# -----------------------------
# Save transformed dataset
# -----------------------------

output_path = os.path.join(current_dir, "..", "data", "processed_sales_data.csv")

df.to_csv(output_path, index=False)

print("\nTransformed dataset saved successfully!")