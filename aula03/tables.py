import sqlite3
from constants import aula03_database

conn = sqlite3.connect(aula03_database)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS category_courses (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        );
    """
)
print("Tabela category_courses criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category_course_id INTEGER NOT NULL
        );
    """
)
print("Tabela courses criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
        );
    """
)
print("Tabela students criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS disciplines (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course_id INTEGER NOT NULL
        );
    """
)
print("Tabela disciplines criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS final_notes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,        
        course_id INTEGER NOT NULL,
        discipline_id INTEGER NOT NULL
        );
    """
)
print("Tabela final_notes criada com sucesso")

conn.close()
