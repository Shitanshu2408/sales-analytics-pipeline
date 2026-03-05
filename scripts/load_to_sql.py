import pandas as pd
import os
from sqlalchemy import create_engine

# locate processed dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", "data", "processed_sales_data.csv")

# read dataset
df = pd.read_csv(file_path)

print("\nDataset preview:")
print(df.head())

# PostgreSQL connection
engine = create_engine("postgresql://postgres:postgres123@localhost:5432/salesdb")

# load dataset to SQL
df.to_sql("sales", engine, if_exists="replace", index=False)

print("\nData successfully loaded into PostgreSQL!")