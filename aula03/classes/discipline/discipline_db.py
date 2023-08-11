import csv
import sqlite3
from typing import List
from constants import aula03_database
from aula03.classes.discipline.discipline import Discipline


def create_disciplines(disciplines: List[Discipline]):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for discipline in disciplines:
        cursor.execute(
            """
            INSERT INTO disciplines (name, course_id)
            VALUES (?, ?) 
            """, (discipline.name, discipline.course_id)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_disciplines():
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    disciplines = cursor.execute(
        """
        SELECT * FROM disciplines;
        """
    )
    disciplines = disciplines.fetchall()
    conn.close()
    return disciplines


def get_disciplines_by_course_id(course_id):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    discipline = cursor.execute(
        f"SELECT * FROM disciplines WHERE course_id = {course_id}"
    )
    discipline = discipline.fetchone()
    conn.close()
    return discipline


def to_csv_disciplines(filename):
    header = ["DISCIPLINA_ID", "DISCIPLINA_NOME"]
    disciplines = get_disciplines()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for discipline in disciplines:
            writer.writerow([
                discipline["id"],
                discipline["name"],
                discipline["course_id"],
            ])

