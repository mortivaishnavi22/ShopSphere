-- Analyze the conversion funnel

SELECT
    event_type,
    COUNT(DISTINCT session_id) AS unique_sessions
FROM events
GROUP BY event_type
ORDER BY
    CASE event_type
        WHEN 'view_product' THEN 1
        WHEN 'add_to_cart' THEN 2
        WHEN 'begin_checkout' THEN 3
        WHEN 'purchase' THEN 4
        ELSE 5
    END;

WITH funnel AS (
    SELECT
        COUNT(DISTINCT CASE
            WHEN event_type = 'view_product'
            THEN session_id END) AS viewed,

        COUNT(DISTINCT CASE
            WHEN event_type = 'add_to_cart'
            THEN session_id END) AS cart,

        COUNT(DISTINCT CASE
            WHEN event_type = 'begin_checkout'
            THEN session_id END) AS checkout,

        COUNT(DISTINCT CASE
            WHEN event_type = 'purchase'
            THEN session_id END) AS purchased
    FROM events
)
SELECT
    viewed,
    cart,
    checkout,
    purchased,

    ROUND(100.0 * cart / NULLIF(viewed, 0), 2)
        AS view_to_cart_pct,

    ROUND(100.0 * checkout / NULLIF(cart, 0), 2)
        AS cart_to_checkout_pct,

    ROUND(100.0 * purchased / NULLIF(checkout, 0), 2)
        AS checkout_to_purchase_pct
FROM funnel;

-- Analyze traffic-source performance
SELECT
    s.traffic_source,
    COUNT(DISTINCT s.session_id) AS total_sessions,
    COUNT(DISTINCT CASE
        WHEN e.event_type = 'purchase'
        THEN s.session_id
    END) AS purchase_sessions,
    ROUND(
        100.0 * COUNT(DISTINCT CASE
            WHEN e.event_type = 'purchase'
            THEN s.session_id
        END) / NULLIF(COUNT(DISTINCT s.session_id), 0),
        2
    ) AS conversion_rate_pct
FROM sessions s
LEFT JOIN events e
    ON s.session_id = e.session_id
GROUP BY s.traffic_source
ORDER BY conversion_rate_pct DESC;

-- Analyze device performance
SELECT
    s.device,
    COUNT(DISTINCT s.session_id) AS total_sessions,
    COUNT(DISTINCT CASE
        WHEN e.event_type = 'purchase'
        THEN s.session_id
    END) AS purchase_sessions,
    ROUND(
        100.0 * COUNT(DISTINCT CASE
            WHEN e.event_type = 'purchase'
            THEN s.session_id
        END) / NULLIF(COUNT(DISTINCT s.session_id), 0),
        2
    ) AS conversion_rate_pct
FROM sessions s
LEFT JOIN events e
    ON s.session_id = e.session_id
GROUP BY s.device
ORDER BY conversion_rate_pct DESC;

-- Analyze revenue and average order value
SELECT
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(oi.quantity * oi.unit_price), 2)
        AS total_revenue,
    ROUND(
        SUM(oi.quantity * oi.unit_price)
        / NULLIF(COUNT(DISTINCT o.order_id), 0),
        2
    ) AS average_order_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'Completed';

-- Analyze product-category revenue
SELECT
    p.category,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2)
        AS total_revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.order_status = 'Completed'
GROUP BY p.category
ORDER BY total_revenue DESC;

