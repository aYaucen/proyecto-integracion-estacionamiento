from flask import Flask, request, jsonify
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
    app.run(port=5000, debug=True)
