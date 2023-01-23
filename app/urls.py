from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),

    # CRUD PLANTAS
    path('listarPlantas', listarPlantas, name = "listarPlantas"),
    path('crearPlantas', crearPlantas, name = "crearPlantas"),
    path('modificarPlantas/<id>', modificarPlantas, name = "modificarPlantas"),
    path('eliminarPlantas/<id>', eliminarPlantas, name = "eliminarPlantas"),
    #----------------------------------------------------------------------------------
    # URL PAGINAS
    path('api', api, name="api"),
    path('carrito', carrito, name="carrito"),
    path('contacto', contacto, name="contacto"),
    path('estadopedido', estadopedido, name="estadopedido"),
    path('estadopedidoadmin', estadopedidoadmin, name="estadopedidoadmin"),
    path('estadopedidousuario', estadopedidousuario, name="estadopedidousuario"),
    path('formulario', formulario, name="formulario"),
    path('formularioSuscripcion', formularioSuscripcion, name="formularioSuscripcion"),
    path('index_formualrioSuscripcion', index_formualrioSuscripcion, name="index_formualrioSuscripcion"),
    path('index_user', index_user, name="index_user"),
    path('login', login, name="login"),
    path('productos', productos, name="productos"),
    path('registration', registration, name="registration"),
    path('suscripcion', suscripcion, name="suscripcion"),
    path('terminos_condiciones', terminos_condiciones, name="terminos_condiciones"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)