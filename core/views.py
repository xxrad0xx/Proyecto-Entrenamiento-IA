from django.shortcuts import render, redirect
from .ml_model import predecir_fahrenheit, obtener_historial

def home(request):
    resultado = None

    if request.method == "POST":
        # Tu formulario usa name="celsius" (ajustamos para que coincida)
        valor = request.POST.get("celsius") or request.POST.get("valor")
        if valor is not None and str(valor).strip() != "":
            try:
                resultado = predecir_fahrenheit(valor)
            except ValueError:
                resultado = None  # Manejo simple si llega algo no numérico

    contexto = {
        "resultado": resultado,
    }
    return render(request, "home.html", contexto)

def about(request):
    historial = obtener_historial()
    history = historial.get("loss", [])
    epochs = len(history)

    return render(request, "about.html", {
        "history": history,
        "epochs": epochs,
    })

def convert(request):
    if request.method == "POST":
        valor = request.POST.get("celsius")
        if valor is None or str(valor).strip() == "":
            return redirect('/')

        try:
            celsius = float(valor)
        except ValueError:
            return redirect('/')

        fahrenheit = predecir_fahrenheit(celsius)

        # Si tu result.html NO usa gráfico, puedes omitir 'history' y 'epochs'
        historial = obtener_historial()
        history = historial.get("loss", [])
        epochs = len(history)

        return render(request, "result.html", {
            "celsius": celsius,
            "fahrenheit": fahrenheit,
            "history": history,
            "epochs": epochs,
        })
    return redirect('/')
