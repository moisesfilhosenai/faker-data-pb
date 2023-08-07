import sqlite3
from constants import aula02_database

conn = sqlite3.connect(aula02_database)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL
        );
    """
)
print("Tabela employees criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS benefits (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL
        );
    """
)
print("Tabela benefits criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS positions (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        salary_base TEXT NOT NULL
        );
    """
)
print("Tabela positions criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS humnan_resources (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        benefit_id INTEGER NOT NULL,
        position_id INTEGER NOT NULL,
        tax TEXT NOT NULL,
        total_hours_late REAL NOT NULL,
        month INTEGER NOT NULL,
        year INTEGER NOT NULL
        );
    """
)
print("Tabela human_resources criada com sucesso")

conn.close()
