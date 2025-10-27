from django.db import models

# Create your models here.
class Paciente(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    codigo_ingreso = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.codigo_ingreso}"
