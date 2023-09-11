import sqlite3
from constants import aula03_database

conn = sqlite3.connect(aula03_database)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


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
        name TEXT NOT NULL
        );
    """
)
print("Tabela disciplines criada com sucesso")


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        discipline_id INTEGER NOT NULL,
        available REAL NOT NULL
        );
    """
)
print("Tabela activities criada com sucesso")


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        activity_id INTEGER NOT NULL,
        available REAL NOT NULL
        );
    """
)
print("Tabela notes criada com sucesso")

conn.close()