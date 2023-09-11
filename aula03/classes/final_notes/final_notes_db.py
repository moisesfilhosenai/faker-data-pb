import csv
import sqlite3
from typing import List
from constants import aula03_database
from aula03.classes.final_notes.final_notes import FinalNotes


def create_final_notes(final_notes: List[FinalNotes]):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for final_note in final_notes:
        cursor.execute(
            """
            INSERT INTO final_notes (student_id, course_id, discipline_id)
            VALUES(?, ?, ?)
            """, (final_note.student_id, final_note.course_id, final_note.discipline_id)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_final_notes():
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    final_notes = cursor.execute(
        """
        SELECT * FROM final_notes;
        """
    )
    final_notes = final_notes.fetchall()
    conn.close()
    return final_notes


def to_csv_final_notes(filename):
    header = ["MEDIA_ID", "ALUNO_ID", "CURSO_ID", "DISCIPLINA_ID"]
    final_notes = get_final_notes()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for final_note in final_notes:
            writer.writerow([
                final_note["id"],
                final_note["student_id"],
                final_note["course_id"],
                final_note["discipline_id"]
            ])