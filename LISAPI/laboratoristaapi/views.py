# Create your views here.
from django.http import JsonResponse
from django.views import View
from .models import Laboratorista
class LaboratoristaView(View):
    def get(self, request):
        laboratoristas = list(Laboratorista.objects.values())
        if laboratoristas:
            return JsonResponse({"message": "Success", "laboratoristas": laboratoristas})
        return JsonResponse({"message": "No hay laboratoristas registrados"})
