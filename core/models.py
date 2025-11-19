from django.db import models

class Prediction(models.Model):
    celsius = models.FloatField()
    pred_fahrenheit = models.FloatField()
    real_fahrenheit = models.FloatField()
    error = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.celsius}°C → {self.pred_fahrenheit:.2f}°F"
