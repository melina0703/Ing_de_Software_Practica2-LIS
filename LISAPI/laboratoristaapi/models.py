from django.db import models

# Create your models here.

class Laboratorista(models.Model):
    codigo_interno = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    titulo_profesional = models.CharField(
        max_length=50,
        choices=[
            ("Bacteriólogo/a", "Bacteriólogo/a"),
            ("Microbiólogo/a", "Microbiólogo/a"),
            ("Biólogo/a", "Biólogo/a"),
        ]
    )
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} ({self.codigo_interno})"

