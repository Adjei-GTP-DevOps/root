from .db import get_connection

def fetch_query(sql):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def top_customers():
    return fetch_query("""
        SELECT c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.customer_id
        ORDER BY total_spent DESC;
    """)

def monthly_sales():
    return fetch_query("""
        SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month,
               SUM(oi.quantity * oi.unit_price) AS total_sales
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.status IN ('Shipped', 'Delivered')
        GROUP BY month
        ORDER BY month;
    """)

def products_never_ordered():
    return fetch_query("""
        SELECT p.name FROM products p
        LEFT JOIN order_items oi ON p.product_id = oi.product_id
        WHERE oi.product_id IS NULL;
    """)

def avg_order_value():
    return fetch_query("""
        SELECT country, AVG(order_total) AS avg_order_value
        FROM (
            SELECT o.order_id, cu.country,
                   SUM(oi.quantity * oi.unit_price) AS order_total
            FROM orders o
            JOIN customers cu ON o.customer_id = cu.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            GROUP BY o.order_id, cu.country
        ) AS order_values
        GROUP BY country;
    """)

def frequent_buyers():
    return fetch_query("""
        SELECT c.name, COUNT(o.order_id) AS order_count
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.customer_id
        HAVING order_count > 1;
    """)
