from django.urls import path    
from .views import PacienteView

urlpatterns = [
    path("pacientes/", PacienteView.as_view(), name="pacientes-view")]