# core/ml_model.py
import numpy as np
from typing import List

# ===== Mini "red": y = w*x + b =====
class TinyLinearNN:
    def __init__(self, w: float, b: float):
        self.w = np.array([[w]], dtype=float)  # (1,1)
        self.b = np.array([b], dtype=float)    # (1,)

    def predict(self, x):
        x = np.array(x, dtype=float).reshape(-1, 1)  # (n,1)
        y = x @ self.w + self.b                       # (n,1)
        return y.ravel()                              # (n,)

# Modelo “entrenado” para C->F
_model = TinyLinearNN(w=9.0/5.0, b=32.0)

# Historial de "loss" (simulado para el gráfico)
_loss_history: List[float] = []

def _build_loss_history(epochs: int = 80) -> List[float]:
    """
    Genera una curva de pérdida decreciente (para visualizar en el gráfico).
    """
    rng = np.random.default_rng(42)
    k = 0.08
    base = np.exp(-k * np.arange(epochs)) * 0.5
    noise = rng.normal(0.0, 0.01, size=epochs)
    h = np.clip(base + noise, 0.0, None)
    return h.tolist()

if not _loss_history:
    _loss_history = _build_loss_history(epochs=80)

# ============================
# FUNCIÓN DE PREDICCIÓN
# ============================
def predecir_fahrenheit(centigrados):
    """
    Convierte grados centígrados a Fahrenheit usando la mini-red.
    """
    valor = float(centigrados)
    resultado = _model.predict([valor])[0]
    return round(float(resultado), 2)

# ============================
# FUNCIÓN PARA GRÁFICAS
# ============================
def obtener_historial():
    """
    Retorna un dict con la misma forma que usabas antes: {"loss": [...]}
    """
    return {"loss": _loss_history}
