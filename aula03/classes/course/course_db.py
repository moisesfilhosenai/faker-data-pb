import csv
import sqlite3
from typing import List
from constants import aula03_database
from aula03.classes.course.course import Course


def create_courses(courses: List[Course]):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for course in courses:
        cursor.execute(
            """
            INSERT INTO courses (name, category_course_id)
            VALUES (?, ?)
            """, (course.name, course.category_course_id)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_courses():
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    courses = cursor.execute(
        """
        SELECT * FROM courses;
        """
    )
    courses = courses.fetchall()
    conn.close()
    return courses


def to_csv_courses(filename):
    header = ["CURSO_ID", "CURSO_NOME"]
    courses = get_courses()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for course in courses:
            writer.writerow([
                course["id"],
                course["name"],
                course["category_course_id"]
            ])
