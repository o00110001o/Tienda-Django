from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('listarPlantas', listarPlantas, name = "listarPlantas"),
    path('crearPlantas', crearPlantas, name = "crearPlantas"),
    path('modificarPlantas/<id>', modificarPlantas, name = "modificarPlantas"),
    path('eliminarPlantas/<id>', eliminarPlantas, name = "eliminarPlantas"),

]
