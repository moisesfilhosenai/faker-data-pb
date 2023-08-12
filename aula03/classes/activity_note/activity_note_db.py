import csv
import sqlite3
from typing import List
from constants import aula03_database
from aula03.classes.activity_note.activity_note import ActivityNote


def create_activities_notes(activities_notes: List[ActivityNote]):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for activities_note in activities_notes:
        cursor.execute(
            """
            INSERT INTO activity_notes (student_id, discipline_id, note, weight)
            VALUES (?, ?, ?, ?)
            """, (activities_note.student_id, activities_note.discipline_id, activities_note.note, activities_note.weight)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_activities_notes():
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    activities_notes = cursor.execute(
        """
        SELECT * FROM activity_notes;
        """
    )
    activities_notes = activities_notes.fetchall()
    conn.close()
    return activities_notes


def to_csv_activities_notes(filename):
    header = ["ATIVIDADE_NOTA_ID", "ALUNO_ID", "DISCIPLINA_ID", "NOTA", "PESO"]
    activities_notes = get_activities_notes()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for activitie_note in activities_notes:
            writer.writerow([
                activitie_note["id"],
                activitie_note["student_id"],
                activitie_note["discipline_id"],
                activitie_note["note"],
                activitie_note["weight"],
            ])