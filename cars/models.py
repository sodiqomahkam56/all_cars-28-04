from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)  # Masalan: Toyota, BMW
    model = models.CharField(max_length=50)  # Masalan: Camry, X5
    year = models.PositiveIntegerField()     # Masalan: 2022
    color = models.CharField(max_length=30)  # Masalan: white, black
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Masalan: 25000.00
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"