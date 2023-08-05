import csv
import sqlite3
from typing import List
from constants import aula01_database
from aula01.classes.customer.customer import Customer


def create_customers(customers: List[Customer]):
    conn = sqlite3.connect(aula01_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for customer in customers:
        cursor.execute(
            """
            INSERT INTO customers (name, zipcode, country, state)
            VALUES (?, ?, ?, ?)
            """, (customer.name, customer.zipcode, customer.country, customer.state)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_customers():
    conn = sqlite3.connect(aula01_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    customers = cursor.execute(
        """
        SELECT * FROM customers;
        """
    )
    customers = customers.fetchall()
    conn.close()
    return customers


def to_csv_customers(filename):
    header = ["CLIENTE_ID", "CLIENTE_NOME", "CLIENTE_CEP",
              "CLIENTE_CIDADE", "CLIENTE_ESTADO"]
    customers = get_customers()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for customer in customers:
            writer.writerow([
                customer["id"],
                customer["name"],
                customer["zipcode"],
                customer["country"],
                customer["state"]
            ])
