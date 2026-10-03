
# ==========================================
# SHOPSPHERE: SYNTHETIC E-COMMERCE DATA
# ==========================================

import sqlite3
import random
from pathlib import Path
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# ------------------------------------------
# 1. CONFIGURATION
# ------------------------------------------

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "shopsphere.db"
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 100
NUM_SESSIONS = 2500

START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2026, 3, 31, 23, 59, 59)

# ------------------------------------------
# 2. HELPER FUNCTIONS
# ------------------------------------------

def random_datetime(start, end):
    """Return a random datetime between two dates."""
    seconds = int((end - start).total_seconds())
    return start + timedelta(seconds=random.randint(0, seconds))


def weighted_choice(options, weights):
    """Select an option using relative probabilities."""
    return random.choices(options, weights=weights, k=1)[0]


# ------------------------------------------
# 3. GENERATE CUSTOMERS
# ------------------------------------------

customers = []

for i in range(1, NUM_CUSTOMERS + 1):
    signup_date = random_datetime(
        START_DATE - timedelta(days=180),
        END_DATE
    )

    customers.append({
        "customer_id": f"CUST{i:04d}",
        "signup_date": signup_date.strftime("%Y-%m-%d"),
        "customer_type": weighted_choice(
            ["New", "Returning"],
            [0.65, 0.35]
        )
    })

customers_df = pd.DataFrame(customers)

# ------------------------------------------
# 4. GENERATE PRODUCTS
# ------------------------------------------

categories = {
    "Electronics": (1500, 45000),
    "Clothing": (300, 5000),
    "Home Appliances": (1000, 25000),
    "Beauty": (150, 3000),
    "Sports": (500, 12000)
}

products = []

for i in range(1, NUM_PRODUCTS + 1):
    category = random.choice(list(categories.keys()))
    low, high = categories[category]

    products.append({
        "product_id": f"PROD{i:03d}",
        "category": category,
        "product_name": f"{category} Product {i:03d}",
        "price": round(random.uniform(low, high), 2)
    })

products_df = pd.DataFrame(products)

# Lookup for quick product access
product_lookup = products_df.set_index("product_id").to_dict("index")
product_ids = products_df["product_id"].tolist()

# ------------------------------------------
# 5. GENERATE SESSIONS AND EVENTS
# ------------------------------------------

devices = ["Mobile", "Desktop", "Tablet"]
device_weights = [0.65, 0.30, 0.05]

sources = [
    "Organic Search", "Paid Search", "Social",
    "Email", "Direct", "Referral"
]
source_weights = [0.30, 0.20, 0.18, 0.10, 0.17, 0.05]

sessions = []
events = []
orders = []
order_items = []

customer_ids = customers_df["customer_id"].tolist()
customer_signup = customers_df.set_index(
    "customer_id"
)["signup_date"].to_dict()

event_id = 1
order_item_id = 1
order_number = 1

for session_num in range(1, NUM_SESSIONS + 1):

    # 80% of sessions are linked to a known customer.
    is_known = random.random() < 0.80

    if is_known:
        customer_id = random.choice(customer_ids)
        visitor_id = "VIS_" + customer_id
    else:
        customer_id = None
        visitor_id = f"ANON_{session_num:05d}"

    session_start = random_datetime(START_DATE, END_DATE)

    # Keep known customers' sessions after signup.
    if customer_id:
        signup = datetime.strptime(
            customer_signup[customer_id], "%Y-%m-%d"
        )
        earliest = max(START_DATE, signup)
        session_start = random_datetime(
            earliest, END_DATE
        )

    session_id = f"SES{session_num:05d}"
    device = weighted_choice(devices, device_weights)
    source = weighted_choice(sources, source_weights)

    sessions.append({
        "session_id": session_id,
        "visitor_id": visitor_id,
        "customer_id": customer_id,
        "session_start": session_start.isoformat(sep=" "),
        "device": device,
        "traffic_source": source
    })

    current_time = session_start

    # A session may view between 1 and 5 products.
    num_views = random.randint(1, 5)
    viewed_products = random.sample(
        product_ids, num_views
    )

    for product_id in viewed_products:
        current_time += timedelta(
            seconds=random.randint(10, 180)
        )

        events.append({
            "event_id": event_id,
            "session_id": session_id,
            "product_id": product_id,
            "event_type": "view_product",
            "event_time": current_time.isoformat(sep=" "),
            "quantity": 1
        })
        event_id += 1

    # Simulate a progressively narrowing purchase funnel.
    # These probabilities are assumptions for our synthetic data.
    if random.random() < 0.40:
        cart_product = random.choice(viewed_products)
        cart_quantity = random.choices(
            [1, 2, 3], weights=[0.80, 0.17, 0.03], k=1
        )[0]

        current_time += timedelta(
            seconds=random.randint(15, 240)
        )

        events.append({
            "event_id": event_id,
            "session_id": session_id,
            "product_id": cart_product,
            "event_type": "add_to_cart",
            "event_time": current_time.isoformat(sep=" "),
            "quantity": cart_quantity
        })
        event_id += 1

        # Only some cart sessions proceed to checkout.
        if random.random() < 0.60:
            current_time += timedelta(
                seconds=random.randint(30, 300)
            )

            events.append({
                "event_id": event_id,
                "session_id": session_id,
                "product_id": cart_product,
                "event_type": "begin_checkout",
                "event_time": current_time.isoformat(sep=" "),
                "quantity": cart_quantity
            })
            event_id += 1

            # Only identified customers can complete orders
            # in this initial version of our data model.
            purchase_probability = 0.65 if customer_id else 0

            if random.random() < purchase_probability:
                current_time += timedelta(
                    seconds=random.randint(60, 600)
                )

                order_id = f"ORD{order_number:05d}"
                order_number += 1

                orders.append({
                    "order_id": order_id,
                    "customer_id": customer_id,
                    "session_id": session_id,
                    "order_date": current_time.isoformat(sep=" "),
                    "order_status": "Completed"
                })

                # The cart product is always included.
                # Additional products may be added to the order.
                purchased_products = [cart_product]

                other_products = [
                    p for p in product_ids
                    if p != cart_product
                ]
                extra_count = random.choices(
                    [0, 1, 2], weights=[0.65, 0.28, 0.07], k=1
                )[0]

                if extra_count:
                    purchased_products.extend(
                        random.sample(other_products, extra_count)
                    )

                for purchased_product in purchased_products:
                    quantity = (
                        cart_quantity
                        if purchased_product == cart_product
                        else random.choices(
                            [1, 2], weights=[0.90, 0.10], k=1
                        )[0]
                    )

                    # Snapshot the price at purchase time.
                    unit_price = product_lookup[
                        purchased_product
                    ]["price"]

                    order_items.append({
                        "order_item_id": order_item_id,
                        "order_id": order_id,
                        "product_id": purchased_product,
                        "quantity": quantity,
                        "unit_price": unit_price
                    })
                    order_item_id += 1

                events.append({
                    "event_id": event_id,
                    "session_id": session_id,
                    "product_id": cart_product,
                    "event_type": "purchase",
                    "event_time": current_time.isoformat(sep=" "),
                    "quantity": cart_quantity
                })
                event_id += 1

# ------------------------------------------
# 6. CREATE DATAFRAMES
# ------------------------------------------

sessions_df = pd.DataFrame(sessions)
events_df = pd.DataFrame(events)
orders_df = pd.DataFrame(orders)
order_items_df = pd.DataFrame(order_items)

# ------------------------------------------
# 7. EXPORT CSV FILES
# ------------------------------------------

dataframes = {
    "customers": customers_df,
    "products": products_df,
    "sessions": sessions_df,
    "events": events_df,
    "orders": orders_df,
    "order_items": order_items_df
}

for name, df in dataframes.items():
    df.to_csv(RAW_DIR / f"{name}.csv", index=False)

# ------------------------------------------
# 8. LOAD INTO SQLITE DATABASE
# ------------------------------------------

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("PRAGMA foreign_keys = ON")

    # Clear previous generated data in dependency order.
    for table in [
        "order_items", "events", "orders",
        "sessions", "products", "customers"
    ]:
        conn.execute(f"DELETE FROM {table}")

    # Insert parent tables before child tables.
    for name in [
        "customers", "products", "sessions",
        "events", "orders", "order_items"
    ]:
        dataframes[name].to_sql(
            name,
            conn,
            if_exists="append",
            index=False
        )

    # Verify row counts in the database.
    print("\nDATABASE ROW COUNTS")
    for table in dataframes:
        count = conn.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]
        print(f"{table:15s}: {count:,}")

# ------------------------------------------
# 9. SUMMARY
# ------------------------------------------

print("\nDATA GENERATION COMPLETE")
print(f"CSV files: {RAW_DIR}")
print(f"SQLite DB: {DB_PATH}")
print(f"Total events: {len(events_df):,}")
print(f"Total orders: {len(orders_df):,}")