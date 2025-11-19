from django.shortcuts import render
from .ml_model import predecir_fahrenheit, obtener_historial

def home(request):
    resultado = None

    if request.method == "POST":
        valor = request.POST.get("valor")
        if valor:
            resultado = predecir_fahrenheit(valor)

    contexto = {
        "resultado": resultado,
    }

    return render(request, "home.html", contexto)

def about(request):
    historial = obtener_historial()

    # Manejo seguro: si no existe "loss", devolvemos lista vacía
    history = historial.get("loss", [])

    # Cantidad de epochs = número de valores de loss
    epochs = len(history)

    return render(request, "about.html", {
        "history": history,
        "epochs": epochs,
    })


def convert(request):
    if request.method == "POST":
        celsius = float(request.POST.get("celsius"))
        fahrenheit = celsius * 1.8 + 32

        return render(request, "result.html", {
            "celsius": celsius,
            "fahrenheit": round(fahrenheit, 2)
        })
    else:
        return render(request, "index.html")