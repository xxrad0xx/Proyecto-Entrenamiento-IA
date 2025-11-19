# ml_model.py
import os
import json
import numpy as np
import tensorflow as tf
from django.conf import settings

# ============================
# RUTAS ABSOLUTAS
# ============================
BASE_DIR = settings.BASE_DIR
MODEL_PATH = os.path.join(BASE_DIR, "modelo", "modelo_temperatura.keras")
HIST_PATH = os.path.join(BASE_DIR, "modelo", "historial_entrenamiento.json")

# ============================
# CARGA DEL MODELO
# ============================
print("Cargando modelo...")

try:
    modelo = tf.keras.models.load_model(MODEL_PATH)
    print("Modelo cargado correctamente.")
except Exception as e:
    print(f"Error cargando el modelo: {e}")
    modelo = None

# ============================
# CARGA DEL HISTORIAL
# ============================
try:
    with open(HIST_PATH, "r") as file:
        historial = json.load(file)
except FileNotFoundError:
    print("❌ No se encontró historial_entrenamiento.json")
    historial = {"loss": []}
except Exception as e:
    print(f"Error cargando historial: {e}")
    historial = {"loss": []}

# ============================
# FUNCIÓN DE PREDICCIÓN
# ============================
def predecir_fahrenheit(centigrados):
    """Convierte grados centígrados a Fahrenheit usando el modelo IA."""
    if modelo is None:
        return None

    valor = float(centigrados)

    resultado = modelo.predict(np.array([[valor]]), verbose=0)
    return round(float(resultado[0][0]), 2)

# ============================
# FUNCIÓN PARA GRÁFICAS
# ============================
def obtener_historial():
    """Retorna el historial completo de entrenamiento."""
    return historial
