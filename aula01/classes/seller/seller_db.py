import csv
import sqlite3
from typing import List
from constants import aula01_database
from aula01.classes.seller.seller import Seller


def create_sellers(sellers: List[Seller]):
    conn = sqlite3.connect(aula01_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for seller in sellers:
        cursor.execute(
            """
            INSERT INTO sellers (name, phone, email, state)
            VALUES (?, ?, ?, ?)
            """, (seller.name, seller.phone, seller.email, seller.state)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_sellers():
    conn = sqlite3.connect(aula01_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sellers = cursor.execute(
        """
        SELECT * FROM sellers;
        """
    )
    sellers = sellers.fetchall()
    conn.close()
    return sellers


def to_csv_sellers(filename):
    header = ["VENDEDOR_ID", "VENDEDOR_NOME", "VENDEDOR_TELEFONE",
              "VENDEDOR_EMAIL", "VENDEDOR_ESTADO"]
    sellers = get_sellers()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for seller in sellers:
            writer.writerow([
                seller["id"],
                seller["name"],
                seller["phone"],
                seller["email"],
                seller["state"]
            ])
