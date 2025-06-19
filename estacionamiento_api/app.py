""" from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)
DATABASE = 'database/estacionamiento.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/ingreso', methods=['POST'])
def ingreso():
    data = request.get_json()
    placa = data.get('placa')
    fecha = datetime.now().strftime('%Y-%m-%d')
    hora_entrada = datetime.now().strftime('%H:%M:%S')

    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO registros (placa, fecha, hora_entrada) VALUES (?, ?, ?)",
            (placa, fecha, hora_entrada))

    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Entrada registrada correctamente"}), 201

@app.route('/salida/<int:id>', methods=['PUT'])
def salida(id):
    hora_salida = datetime.now().strftime('%H:%M:%S')
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE registros SET hora_salida = ? WHERE id = ?", (hora_salida, id))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Salida registrada correctamente"})

@app.route('/registros', methods=['GET'])
def registros():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM registros")
    rows = cur.fetchall()
    registros = [dict(row) for row in rows]
    conn.close()
    return jsonify(registros)

if __name__ == '__main__':
    app.run(port=5000, debug=True) """

# estacionamiento_api/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

DATABASE = 'database/estacionamiento.db'

# ---------------------------
# Función reutilizable para DB
# ---------------------------
def execute_query(query, params=(), fetch=False):
    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, params)
        if fetch:
            return [dict(row) for row in cur.fetchall()]
        conn.commit()

# ---------------------------
# Endpoint: Registrar ingreso
# ---------------------------
@app.route('/ingreso', methods=['POST'])
def ingreso():
    data = request.get_json()
    placa = data.get('placa')

    if not placa:
        return jsonify({"error": "Placa no proporcionada"}), 400

    fecha = datetime.now().strftime('%Y-%m-%d')
    hora_entrada = datetime.now().strftime('%H:%M:%S')

    execute_query(
        "INSERT INTO registros (placa, fecha, hora_entrada) VALUES (?, ?, ?)",
        (placa, fecha, hora_entrada)
    )

    return jsonify({"mensaje": "Entrada registrada correctamente"}), 201

# ---------------------------
# Endpoint: Registrar salida
# ---------------------------
@app.route('/salida/<int:id>', methods=['PUT'])
def salida(id):
    # Verificar si ya tiene hora_salida
    result = execute_query("SELECT hora_salida FROM registros WHERE id = ?", (id,), fetch=True)
    if not result:
        return jsonify({"error": "Registro no encontrado"}), 404
    if result[0]["hora_salida"]:
        return jsonify({"mensaje": "La salida ya fue registrada"}), 400

    hora_salida = datetime.now().strftime('%H:%M:%S')
    execute_query("UPDATE registros SET hora_salida = ? WHERE id = ?", (hora_salida, id))
    return jsonify({"mensaje": "Salida registrada correctamente"})

# ---------------------------
# Endpoint: Listar todos los registros
# ---------------------------
@app.route('/registros', methods=['GET'])
def registros():
    result = execute_query("SELECT * FROM registros", fetch=True)
    return jsonify(result)

# ---------------------------
# Endpoint: Obtener registro por ID
# ---------------------------
@app.route('/registro/<int:id>', methods=['GET'])
def obtener_registro(id):
    result = execute_query("SELECT * FROM registros WHERE id = ?", (id,), fetch=True)
    if not result:
        return jsonify({"error": "Registro no encontrado"}), 404
    return jsonify(result[0])

# ---------------------------
# Iniciar la aplicación
# ---------------------------
if __name__ == '__main__':
    os.makedirs('database', exist_ok=True)
    app.run(port=5000, debug=True)
