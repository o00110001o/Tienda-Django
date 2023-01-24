from django.urls import path
from rest_planta.views import detalle_planta, lista_plantas

urlpatterns = [

    path('lista_plantas', lista_plantas, name="lista_plantas"),
    path('detalle_planta/<id>', detalle_planta, name="detalle_planta"),
]