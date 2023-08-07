import csv
import sqlite3
from typing import List
from constants import aula02_database
from aula02.classes.humnan_resources.human_resource import HumnanResource


def create_humnan_resources(humnan_resouces: List[HumnanResource]):
    conn = sqlite3.connect(aula02_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for humnan_resouce in humnan_resouces:
        cursor.execute(
            """
            INSERT INTO humnan_resources (employee_id, benefit_id, position_id, tax, total_hours_late, month, year)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (humnan_resouce.employee_id, humnan_resouce.benefit_id, humnan_resouce.position_id,
                  humnan_resouce.tax, humnan_resouce.total_hours_late, humnan_resouce.month, humnan_resouce.year)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_humnan_resources():
    conn = sqlite3.connect(aula02_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    humnan_resouces = cursor.execute(
        """
        SELECT * FROM humnan_resources;
        """
    )
    humnan_resouces = humnan_resouces.fetchall()
    conn.close()
    return humnan_resouces


def to_csv_humnan_resouces(filename):
    header = [
        "ID", "FUNCIONARIO", "CODIGO BENEFICIO", "FUNCAO_ID", "INSS", "TOTAL_HORAS_ATRASO", "MES", "YEAR"
    ]
    humnan_resouces = get_humnan_resources()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for humnan_resouce in humnan_resouces:
            writer.writerow([
                humnan_resouce["id"],
                humnan_resouce["employee_id"],
                humnan_resouce["benefit_id"],
                humnan_resouce["position_id"],
                humnan_resouce["tax"],
                humnan_resouce["total_hours_late"],
                humnan_resouce["month"],
                humnan_resouce["year"],
            ])
