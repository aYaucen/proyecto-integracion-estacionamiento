""" import sqlite3

conn = sqlite3.connect('database/estacionamiento.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    placa TEXT,
    fecha TEXT,
    hora_entrada TEXT,
    hora_salida TEXT
)
''')
conn.commit()
conn.close()
print("Base de datos inicializada correctamente.") """

# estacionamiento_api/utils/db_init.py
import sqlite3
import os

# Asegura que la carpeta 'database' exista
os.makedirs('database', exist_ok=True)

conn = sqlite3.connect('database/estacionamiento.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    placa TEXT NOT NULL,
    fecha TEXT NOT NULL,
    hora_entrada TEXT NOT NULL,
    hora_salida TEXT
)
''')

conn.commit()
conn.close()
print("✅ Base de datos inicializada correctamente.")
