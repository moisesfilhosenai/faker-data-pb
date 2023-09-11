import csv
import sqlite3
from typing import List
from constants import aula03_database
from aula03.classes.notes.note import Note


def create_notes(notes: List[Note]):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for note in notes:
        cursor.execute(
            """
            INSERT INTO notes (student_id, activity_id, available)
            VALUES (?, ?, ?)
            """, (note.student_id, note.activity_id, note.available)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_notes():
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    notes = cursor.execute(
        """
        SELECT * FROM notes;
        """
    )
    notes = notes.fetchall()
    conn.close()
    return notes


def to_csv_notes(filename):
    header = ["ALUNO_ID", "ATIVIDADE_ID", "NOTA"]
    notes = get_notes()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)

        for note in notes:
            writer.writerow([
                note["student_id"],
                note["activity_id"],
                note["available"]
            ])