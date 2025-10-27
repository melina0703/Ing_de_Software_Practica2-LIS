from django.db import models
from pacientes.models import Paciente
from laboratoristaapi.models import Laboratorista

# Create your models here.

class Resultado(models.Model):
    codigo_ingreso = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="resultados")
    colesterol_total = models.FloatField()
    colesterol_hdl = models.FloatField()
    colesterol_ldl = models.FloatField()
    trigliceridos = models.FloatField()
    laboratorista = models.ForeignKey(Laboratorista, on_delete=models.SET_NULL, null=True, related_name="resultados")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resultado {self.codigo_ingreso} - {self.laboratorista}"
