import csv
import sqlite3
from typing import List
from constants import aula02_database
from aula02.classes.position.position import Position


def create_positions(positions: List[Position]):
    conn = sqlite3.connect(aula02_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for position in positions:
        cursor.execute(
            """
            INSERT INTO positions (name, salary_base)
            VALUES (?, ?)
            """, (position.name, position.salary_base)
        )

    cursor.close()
    conn.commit()
    conn.close()


def get_positions():
    conn = sqlite3.connect(aula02_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    positions = cursor.execute(
        """
        SELECT * FROM positions;
        """
    )
    positions = positions.fetchall()
    conn.close()
    return positions


def to_csv_positions(filename):
    header = ["CARGO_ID", "CARGO_NOME", "CARGO_SALARIO_BASE"]
    roles = get_positions()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for role in roles:
            writer.writerow([
                role["id"],
                role["name"],
                role["salary_base"]
            ])
