from fastapi import FastAPI
from app import queries

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": """MySQL Store API is live.
            Available endpoints:
            - /top-customers: Returns customers ranked by total spending
            - /monthly-sales: Shows monthly sales for shipped/delivered orders
            - /products-never-ordered: Lists products that have never been ordered
            - /avg-order-value: Displays average order value by country
            - /frequent-buyers: Shows customers who have placed more than one order
            """}

@app.get("/top-customers")
def top_customers():
    return queries.top_customers()

@app.get("/monthly-sales")
def monthly_sales():
    return queries.monthly_sales()

@app.get("/products-never-ordered")
def products_never_ordered():
    return queries.products_never_ordered()

@app.get("/avg-order-value")
def avg_order_value():
    return queries.avg_order_value()

@app.get("/frequent-buyers")
def frequent_buyers():
    return queries.frequent_buyers()
