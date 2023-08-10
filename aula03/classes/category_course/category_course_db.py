import csv
import sqlite3
from typing import List
from constants import aula03_database
from aula03.classes.category_course.category_course import CategoryCourse


def create_categories_courses(categories_courses: List[CategoryCourse]):
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    for category in categories_courses:
        cursor.execute(
            """
            INSERT INTO category_courses (name)
            VALUES (?)
            """, (category.name,)
        )
    cursor.close()
    conn.commit()
    conn.close()


def get_categories_courses():
    conn = sqlite3.connect(aula03_database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    categories_courses = cursor.execute(
        """
        SELECT * FROM category_courses;
        """
    )
    categories_courses = categories_courses.fetchall()
    conn.close()
    return categories_courses


def to_csv_categories_courses(filename):
    header = ["CATEGORIA_ID", "CATEGORIA_NOME"]
    categories_courses = get_categories_courses()

    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for categories_course in categories_courses:
            writer.writerow([
                categories_course["id"],
                categories_course["name"],

            ])
