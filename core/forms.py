from django import forms

class TemperatureForm(forms.Form):
    celsius = forms.FloatField(
        label="Temperatura en °C",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Ej: 17"
        })
    )
