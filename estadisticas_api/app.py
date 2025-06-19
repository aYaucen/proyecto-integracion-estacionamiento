""" from flask import Flask, jsonify
from flask_cors import CORS
from services.estadisticas import dia_mas_ocupado, promedio_diario

app = Flask(__name__)
CORS(app)

@app.route('/estadisticas/dia-mas-ocupado', methods=['GET'])
def ruta_dia_mas_ocupado():
    return jsonify(dia_mas_ocupado())

@app.route('/estadisticas/promedio-diario', methods=['GET'])
def ruta_promedio_diario():
    return jsonify(promedio_diario())

@app.route('/')
def inicio():
    return jsonify({"mensaje": "API de estadísticas activa"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
 """

# estadistica_api/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from services.estadisticas import dia_mas_ocupado, promedio_diario

app = Flask(__name__)
CORS(app)

@app.route('/')
def inicio():
    return jsonify({"mensaje": "✅ API de estadísticas activa"})

@app.route('/estadisticas/dia-mas-ocupado', methods=['GET'])
def ruta_dia_mas_ocupado():
    resultado = dia_mas_ocupado()
    return jsonify(resultado)

@app.route('/estadisticas/promedio-diario', methods=['GET'])
def ruta_promedio_diario():
    resultado = promedio_diario()
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
