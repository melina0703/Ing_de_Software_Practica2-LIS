from django.http import JsonResponse
from django.views import View
from .models import Paciente

class PacienteView(View):
    def get(self, request):
        pacientes = list(Paciente.objects.values())
        if len(pacientes) > 0:
            datos={"message":"Success","pacientes":pacientes}
        else:    
            datos={"message":"No hay pacientes registrados"}
        return JsonResponse(datos)
