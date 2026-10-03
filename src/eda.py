import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "shopsphere.db"
OUTPUT_DIR = BASE_DIR / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)

# Load tables
customers = pd.read_sql_query("SELECT * FROM customers", conn)
products = pd.read_sql_query("SELECT * FROM products", conn)
sessions = pd.read_sql_query("SELECT * FROM sessions", conn)
events = pd.read_sql_query("SELECT * FROM events", conn)
orders = pd.read_sql_query("SELECT * FROM orders", conn)
order_items = pd.read_sql_query("SELECT * FROM order_items", conn)

print("Events columns:", events.columns.tolist())
print("Sessions columns:", sessions.columns.tolist())
print("Orders columns:", orders.columns.tolist())

# Count distinct sessions for each funnel event
funnel = (
    events.groupby("event_type")["session_id"]
    .nunique()
    .reindex(
        ["view_product", "add_to_cart",
         "begin_checkout", "purchase"],
        fill_value=0
    )
)

print("\n--- FUNNEL BY DISTINCT SESSIONS ---")
print(funnel)

# Check whether sessions have expected event sequences
event_sets = (
    events.groupby("session_id")["event_type"]
    .agg(set)
)

print("\nCheckout sessions:", (event_sets.apply(
    lambda x: "begin_checkout" in x
)).sum())

print("Purchase sessions:", (event_sets.apply(
    lambda x: "purchase" in x
)).sum())

print("Purchase sessions without cart:",
      (event_sets.apply(
          lambda x: "purchase" in x and "add_to_cart" not in x
      )).sum())

# Check missing values and duplicates
tables = {
    "customers": customers,
    "products": products,
    "sessions": sessions,
    "events": events,
    "orders": orders,
    "order_items": order_items
}

for name, df in tables.items():
    print(f"\n--- {name.upper()} ---")
    print("Rows and columns:", df.shape)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

conn.close()

# Convert date columns
date_columns = {
    "customers": (customers, ["signup_date"]),
    "sessions": (sessions, ["session_start"]),
    "events": (events, ["event_time"]),
    "orders": (orders, ["order_date"])
}

for table_name, (df, columns) in date_columns.items():
    for column in columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )
            print(f"Converted {table_name}.{column} to datetime")
        else:
            print(
                f"WARNING: {table_name} does not contain "
                f"'{column}'. Available columns: {df.columns.tolist()}"
            )

print("Data loaded successfully!")
print("Customers:", customers.shape)
print("Products:", products.shape)
print("Sessions:", sessions.shape)
print("Events:", events.shape)
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)

# Customer overview
print("\nCustomer types:")
print(customers["customer_type"].value_counts(dropna=False))

# Product overview
print("\nProducts by category:")
print(products["category"].value_counts())

# Session overview
print("\nSessions by device:")
print(sessions["device"].value_counts())

print("\nSessions by traffic source:")
print(sessions["traffic_source"].value_counts())

# Event overview
print("\nEvent types:")
print(events["event_type"].value_counts())

# Order overview
print("\nOrder status:")
print(orders["order_status"].value_counts())

# Visualize the data------------------------------------------------
sns.set_theme()

# 1. Sessions by device
plt.figure(figsize=(8, 5))
sns.countplot(data=sessions, x="device")
plt.title("Sessions by Device")
plt.xlabel("Device")
plt.ylabel("Number of Sessions")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sessions_by_device.png")
plt.show()

# 2. Events by type
plt.figure(figsize=(9, 5))
sns.countplot(
    data=events,
    x="event_type",
    order=events["event_type"].value_counts().index
)
plt.title("Distribution of E-commerce Events")
plt.xlabel("Event Type")
plt.ylabel("Number of Events")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "events_by_type.png")
plt.show()

# 3. Products by category
plt.figure(figsize=(10, 5))
category_counts = products["category"].value_counts()
sns.barplot(x=category_counts.index, y=category_counts.values)
plt.title("Number of Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "products_by_category.png")
plt.show()


# Calculate initial business KPIs --------------------------------------------------------------------------------------------
total_sessions = sessions["session_id"].nunique()

purchase_sessions = events.loc[
    events["event_type"] == "purchase",
    "session_id"
].nunique()

cart_sessions = events.loc[
    events["event_type"] == "add_to_cart",
    "session_id"
].nunique()

checkout_sessions = events.loc[
    events["event_type"] == "begin_checkout",
    "session_id"
].nunique()

conversion_rate = (
    purchase_sessions / total_sessions * 100
    if total_sessions else 0
)

cart_rate = (
    cart_sessions / total_sessions * 100
    if total_sessions else 0
)

cart_abandonment_rate = (
    (cart_sessions - purchase_sessions) / cart_sessions * 100
    if cart_sessions else 0
)

print("\n--- INITIAL KPIs ---")
print(f"Total sessions: {total_sessions}")
print(f"Sessions with cart events: {cart_sessions}")
print(f"Sessions with checkout events: {checkout_sessions}")
print(f"Sessions with purchase events: {purchase_sessions}")
print(f"Session conversion rate: {conversion_rate:.2f}%")
print(f"Session add-to-cart rate: {cart_rate:.2f}%")
print(f"Approx. cart abandonment rate: {cart_abandonment_rate:.2f}%")

# Save cleaned data --------------------------------------------------------
cleaned_tables = {
    "customers": customers.copy(),
    "products": products.copy(),
    "sessions": sessions.copy(),
    "events": events.copy(),
    "orders": orders.copy(),
    "order_items": order_items.copy()
}

# Standardize text columns
for df in cleaned_tables.values():
    for column in df.columns:
        if (
            df[column].dtype == "object"
            or isinstance(df[column].dtype, pd.StringDtype)
        ):
            df[column] = df[column].str.strip()

# Save cleaned CSV files
CLEAN_DIR = BASE_DIR / "data" / "processed"
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

for name, df in cleaned_tables.items():
    df.to_csv(CLEAN_DIR / f"{name}_cleaned.csv", index=False)

print("\nCleaned CSV files saved to:", CLEAN_DIR)

# ---------------------------------------------------------------------------------