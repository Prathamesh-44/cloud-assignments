# Self 9: multi-tenant records; every query is filtered by customer_id
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id TEXT, item TEXT, amount REAL)")
db.executemany("INSERT INTO orders(customer_id,item,amount) VALUES (?,?,?)", [
    ("cust_A", "Laptop", 55000), ("cust_A", "Mouse", 700),
    ("cust_B", "Phone", 30000), ("cust_B", "Charger", 900)])


def get_orders(customer_id):
    """A tenant can only ever see rows with their own customer_id."""
    return db.execute("SELECT id,item,amount FROM orders WHERE customer_id=?", (customer_id,)).fetchall()


for cust in ("cust_A", "cust_B"):
    print(cust, "->", get_orders(cust))
print("cust_C ->", get_orders("cust_C"))      # unknown tenant sees nothing
