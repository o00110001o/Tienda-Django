from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('api', api, name="api"),
    path('carrito', carrito, name="carrito"),
    path('contacto', contacto, name="contacto"),
    path('estadopedido', estadopedido, name="estadopedido"),
    path('estadopedidoadmin', estadopedidoadmin, name="estadopedidoadmin"),
    path('estadopedidousuario', estadopedidousuario, name="estadopedidousuario"),
    path('formulario', formulario, name="formulario"),
    path('formularioSuscripcion', formularioSuscripcion, name="formularioSuscripcion"),
    path('index_formualrioSuscripcion', index_formualrioSuscripcion, name="index_formualrioSuscripcion"),
    path('/', , name=""),
    path('/', , name=""),
    path('/', , name=""),
    path('/', , name=""),
    path('/', , name=""),
    path('/', , name=""),
]
