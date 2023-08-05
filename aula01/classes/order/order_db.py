import csv
import sqlite3
from typing import List
from constants import aula01_database
from aula01.classes.order.order import Order


def create_orders(orders: List[Order]):
    conn = sqlite3.connect(aula01_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for order in orders:
        cursor.execute(
            """
            INSERT INTO orders (data, customer_id, seller_id, product_id, quantity, price)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (order.data, order.customer_id, order.seller_id,
                  order.produt_id, order.quantity, order.price)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_orders():
    conn = sqlite3.connect(aula01_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sellers = cursor.execute(
        """
        SELECT * FROM orders;
        """
    )
    sellers = sellers.fetchall()
    conn.close()
    return sellers


def to_csv_orders(filename):
    header = [
        "PEDIDO_ID", "PEDIDO_DATA", "COD CLIENTE", "COD_VENDEDOR",
        "COD PRODUTO", "QUANTIDADE PRODUTO", "VALOR PRODUTO"
    ]
    orders = get_orders()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for order in orders:
            writer.writerow([
                order["id"],
                order["data"],
                order["customer_id"],
                order["seller_id"],
                order["product_id"],
                order["quantity"],
                order["price"]
            ])
