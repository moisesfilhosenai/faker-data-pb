import csv
import sqlite3
from typing import List
from constants import aula03_database
from aula03.classes.student.student import Student


def create_students(students: List[Student]):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for student in students:
        cursor.execute(
            """
            INSERT INTO students (name, email)
            VALUES (?, ?)
            """, (student.name, student.email)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_students():
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    students = cursor.execute(
        """
        SELECT * FROM students;
        """
    )
    students = students.fetchall()
    conn.close()
    return students


def to_csv_students(filename):
    header = ["ALUNO_ID", "ALUNO_NOME", "ALUNO_EMAIL"]
    students = get_students()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for student in students:
            writer.writerow([
                student["id"],
                student["name"],
                student["email"]
            ])