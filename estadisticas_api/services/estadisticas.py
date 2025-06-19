import requests
from collections import Counter

REGISTROS_URL = 'http://localhost:5000/registros'

def obtener_registros():
    response = requests.get(REGISTROS_URL)
    return response.json()

def dia_mas_ocupado():
    data = obtener_registros()
    fechas = [r['fecha'] for r in data]
    conteo = Counter(fechas)
    if not conteo:
        return {"dia": None, "total": 0}
    mas_ocupado = conteo.most_common(1)[0]
    return {"dia": mas_ocupado[0], "total": mas_ocupado[1]}

def promedio_diario():
    data = obtener_registros()
    fechas = [r['fecha'] for r in data]
    conteo = Counter(fechas)
    promedio = sum(conteo.values()) / len(conteo) if conteo else 0
    return {"promedio_diario": round(promedio, 2)}
