import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

st.title("📊 Sales Analytics Dashboard")

engine = create_engine("postgresql://postgres:postgres123@localhost:5432/salesdb")


# ---------------------------
# Load Data
# ---------------------------

@st.cache_data
def load_data():
    query = "SELECT * FROM sales"
    return pd.read_sql(query, engine)

df = load_data()


# ---------------------------
# Sidebar Filters
# ---------------------------

st.sidebar.header("Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["region"].unique(),
    default=df["region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["category"].unique(),
    default=df["category"].unique()
)

month_filter = st.sidebar.multiselect(
    "Select Month",
    options=df["month"].unique(),
    default=df["month"].unique()
)


# ---------------------------
# Apply Filters
# ---------------------------

filtered_df = df[
    (df["region"].isin(region_filter)) &
    (df["category"].isin(category_filter)) &
    (df["month"].isin(month_filter))
]


# ---------------------------
# KPI Metrics
# ---------------------------

total_revenue = filtered_df["revenue"].sum()
total_orders = filtered_df["order_id"].count()
products = filtered_df["product"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,}")
col2.metric("📦 Total Orders", total_orders)
col3.metric("🛍 Products Sold", products)


# ---------------------------
# Charts
# ---------------------------

st.subheader("Top Selling Products")

product_sales = filtered_df.groupby("product")["revenue"].sum().sort_values(ascending=False)
st.bar_chart(product_sales)


st.subheader("Revenue by Region")

region_sales = filtered_df.groupby("region")["revenue"].sum().sort_values(ascending=False)
st.bar_chart(region_sales)


st.subheader("Category Performance")

category_sales = filtered_df.groupby("category")["revenue"].sum().sort_values(ascending=False)
st.bar_chart(category_sales)


st.subheader("Monthly Revenue Trend")

month_sales = filtered_df.groupby("month")["revenue"].sum()
st.line_chart(month_sales)


# ---------------------------
# Raw Data
# ---------------------------

st.subheader("Filtered Sales Data")
st.dataframe(filtered_df)