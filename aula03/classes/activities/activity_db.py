import csv
import sqlite3
from typing import List
from constants import aula03_database
from aula03.classes.activities.activity import Activity


def create_activities(activities: List[Activity]):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for activity in activities:
        cursor.execute(
            """
            INSERT INTO activities (description, discipline_id, available)
            VALUES (?, ?, ?)
            """, (activity.description, activity.discipline_id, activity.available)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_activities():
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    activities = cursor.execute(
        """
        SELECT * FROM activities;
        """
    )
    activities = activities.fetchall()
    conn.close()
    return activities


def to_csv_activities(filename):
    header = ["ATIVIDADE_ID", "ATIVIDADE_DESCRIÇÃO", "DISCIPLINA_ID", "NOTA_MAXIMA"]
    activities = get_activities()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)

        for activity in activities:
            writer.writerow([
                activity["id"],
                activity["description"],
                activity["discipline_id"],
                activity["available"]
            ])