from django.urls import path
from .views import  ResultadoView

urlpatterns = [
    path('resultados/', ResultadoView.as_view(), name='resultados'),
]