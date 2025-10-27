from django.http import JsonResponse
from django.views import View
from .models import Resultado

class ResultadoView(View):
    def get(self, request):
        resultados = list(Resultado.objects.values())
        if resultados:
            return JsonResponse({"message": "Success", "resultados": resultados})
        return JsonResponse({"message": "No hay resultados registrados"})


