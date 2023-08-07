import csv
import sqlite3
from typing import List
from constants import aula02_database
from aula02.classes.benefit.benefit import Benefit


def create_benefits(benefits: List[Benefit]):
    conn = sqlite3.connect(aula02_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for benefit in benefits:
        cursor.execute(
            """
            INSERT INTO benefits (name, price)
            VALUES (?, ?)
            """, (benefit.name, benefit.price)
        )

    cursor.close()
    conn.commit()
    conn.close()


def get_benefits():
    conn = sqlite3.connect(aula02_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    benefits = cursor.execute(
        """
        SELECT * FROM benefits;
        """
    )
    benefits = benefits.fetchall()
    conn.close()
    return benefits


def to_csv_benefits(filename):
    header = ["BENEFICIO_ID", "BENEFICIO_NOME", "BENEFICIO_VALOR"]
    benefits = get_benefits()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for benefit in benefits:
            writer.writerow([
                benefit["id"],
                benefit["name"],
                benefit["price"]
            ])
