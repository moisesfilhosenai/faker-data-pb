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
