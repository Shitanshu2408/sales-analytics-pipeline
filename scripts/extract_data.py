import pandas as pd
import os

# Get current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build path to CSV
file_path = os.path.join(current_dir, "..", "data", "raw_sales_data.csv")

# Read CSV
df = pd.read_csv(file_path)

print("Raw Data:")
print(df.head())