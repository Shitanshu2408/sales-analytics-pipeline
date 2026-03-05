import pandas as pd
import os

# Get script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build dataset path
file_path = os.path.join(current_dir, "..", "data", "raw_sales_data.csv")

# Load dataset
df = pd.read_csv(file_path)

print("\n===== ORIGINAL DATA =====")
print(df.head())

# -------------------------------
# 1️⃣ Check Missing Values
# -------------------------------

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# -------------------------------
# 2️⃣ Remove Duplicates
# -------------------------------

duplicates = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")

df = df.drop_duplicates()

# -------------------------------
# 3️⃣ Fix Data Types
# -------------------------------

df["date"] = pd.to_datetime(df["date"])

# -------------------------------
# 4️⃣ Basic Statistics
# -------------------------------

print("\n===== DATA SUMMARY =====")
print(df.describe())

# -------------------------------
# 5️⃣ Validate Business Rules
# -------------------------------

invalid_rows = df[(df["quantity"] <= 0) | (df["price"] <= 0)]

print("\nInvalid rows (if any):")
print(invalid_rows)

print("\n===== CLEANED DATA =====")
print(df.head())