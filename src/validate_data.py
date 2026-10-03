
import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "shopsphere.db"

with sqlite3.connect(DB_PATH) as conn:
    # Load each table for validation
    tables = [
        "customers", "products", "sessions",
        "events", "orders", "order_items"
    ]

    data = {
        table: pd.read_sql_query(
            f"SELECT * FROM {table}", conn
        )
        for table in tables
    }

    # 1. Row counts
    print("1. ROW COUNTS")
    for name, df in data.items():
        print(f"{name}: {len(df):,}")

    # 2. Missing values
    print("\n2. MISSING VALUES")
    for name, df in data.items():
        missing = df.isna().sum()
        print(f"\n{name}")
        print(missing[missing > 0])

    # 3. Duplicate primary keys
    print("\n3. DUPLICATE IDENTIFIERS")
    primary_keys = {
        "customers": "customer_id",
        "products": "product_id",
        "sessions": "session_id",
        "events": "event_id",
        "orders": "order_id",
        "order_items": "order_item_id"
    }

    for name, key in primary_keys.items():
        duplicates = data[name][key].duplicated().sum()
        print(f"{name}: {duplicates}")

    # 4. Foreign key integrity
    print("\n4. FOREIGN KEY CHECK")
    for table, rows in conn.execute(
        "PRAGMA foreign_key_check"
    ):
        print(f"Violation in {table}, row {rows}")

    print("No output above means no FK violations.")

    # 5. Event type distribution
    print("\n5. EVENT DISTRIBUTION")
    print(
        data["events"]["event_type"]
        .value_counts()
        .to_string()
    )

    # 6. Order revenue
    print("\n6. REVENUE SUMMARY")
    items = data["order_items"].copy()
    items["line_revenue"] = (
        items["quantity"] * items["unit_price"]
    )
    print(f"Total revenue: ₹{items['line_revenue'].sum():,.2f}")
    print(f"Order count: {data['orders']['order_id'].nunique():,}")