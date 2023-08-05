import csv
import sqlite3
from typing import List
from constants import aula01_database
from aula01.classes.product.product import Product


def create_products(products: List[Product]):
    conn = sqlite3.connect(aula01_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for product in products:
        cursor.execute(
            """
            INSERT INTO products (name, category, price)
            VALUES (?, ?, ?)
            """, (product.name, product.category, product.price)
        )
    cursor.close()
    conn.commit()


def get_products():
    conn = sqlite3.connect(aula01_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    products = cursor.execute(
        """
        SELECT * FROM products;
        """
    )
    products = products.fetchall()
    conn.close()
    return products


def to_csv_products(filename):
    header = ["PRODUTO_ID", "PRODUTO_NOME", "PRODUTO_CATEGORIA"]
    products = get_products()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for product in products:
            writer.writerow([
                product["id"],
                product["name"],
                product["category"]
            ])
