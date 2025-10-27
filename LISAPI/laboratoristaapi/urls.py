from django.urls import path
from .views import  LaboratoristaView

urlpatterns = [
    path('laboratoristas/', LaboratoristaView.as_view(), name='laboratoristas'),
    
]