import sqlite3
from constants import aula01_database

conn = sqlite3.connect(aula01_database)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
        );
    """
)
print("Tabela products criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        zipcode TEXT NOT NULL,
        country TEXT NOT NULL,
        state TEXT NOT NULL
        );
    """
)
print("Tabela customers criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sellers (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        state TEXT NOT NULL
        );
    """
)
print("Tabela sellers criada com sucesso")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        customer_id INTEGER NOT NULL,
        seller_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
        );
    """
)
print("Tabela orders criada com sucesso")

conn.close()
