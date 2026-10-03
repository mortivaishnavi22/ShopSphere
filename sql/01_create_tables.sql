PRAGMA foreign_keys = ON;

-- 1. Customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    signup_date TEXT,
    customer_type TEXT
);

-- 2. Products
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    category TEXT NOT NULL,
    product_name TEXT,
    price REAL CHECK (price >= 0)
);

-- 3. Website sessions
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    visitor_id TEXT NOT NULL,
    customer_id TEXT,
    session_start TEXT NOT NULL,
    device TEXT,
    traffic_source TEXT,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- 4. Customer interaction events
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY,
    session_id TEXT NOT NULL,
    product_id TEXT,
    event_type TEXT NOT NULL,
    event_time TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    FOREIGN KEY (session_id)
        REFERENCES sessions(session_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id),
    CHECK (quantity > 0)
);

-- 5. Completed orders
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    session_id TEXT NOT NULL,
    order_date TEXT NOT NULL,
    order_status TEXT NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),
    FOREIGN KEY (session_id)
        REFERENCES sessions(session_id)
);

-- 6. Order line items
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id TEXT NOT NULL,
    product_id TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id),
    CHECK (quantity > 0),
    CHECK (unit_price >= 0)
);

-- Useful indexes for analysis
CREATE INDEX IF NOT EXISTS idx_events_session
ON events(session_id);

CREATE INDEX IF NOT EXISTS idx_events_type_time
ON events(event_type, event_time);

CREATE INDEX IF NOT EXISTS idx_sessions_visitor
ON sessions(visitor_id);

CREATE INDEX IF NOT EXISTS idx_orders_customer
ON orders(customer_id);