import csv
import sqlite3
from typing import List
from constants import aula02_database
from aula02.classes.employee.employee import Employee


def create_employees(employees: List[Employee]):
    conn = sqlite3.connect(aula02_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for employee in employees:
        cursor.execute(
            """
            INSERT INTO employees (name, address)
            VALUES (?, ?)
            """, (employee.name, employee.address)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_employees():
    conn = sqlite3.connect(aula02_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    employees = cursor.execute(
        """
        SELECT * FROM employees;
        """
    )
    employees = employees.fetchall()
    conn.close()
    return employees


def to_csv_employees(filename):
    header = ["FUNCIONARIO_ID", "FUNCIONARIO_NOME", "FUNCIONARIO_ENDERECO"]
    employees = get_employees()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for employee in employees:
            writer.writerow([
                employee["id"],
                employee["name"],
                employee["address"]
            ])
