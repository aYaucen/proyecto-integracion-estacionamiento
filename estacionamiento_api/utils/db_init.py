import sqlite3

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
print("Base de datos inicializada correctamente.")
