SELECT 
    country,
    AVG(order_total) AS avg_order_value
FROM (
    SELECT 
        o.order_id, 
        cu.country,
        SUM(oi.quantity * oi.unit_price) AS order_total
    FROM orders o
    JOIN customers cu ON o.customer_id = cu.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY o.order_id, cu.country
) AS order_values
GROUP BY country;
