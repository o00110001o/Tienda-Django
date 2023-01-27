from django.urls import path 
from api_app.views import lista_plantas, detalle_planta
from api_app.viewslogin import login
from viewslogin import *
urlpatterns = [
    path('lista_plantas', lista_plantas, name="lista_plantas"),
    path('detalle_planta/<id>', detalle_planta, name="detalle_planta"),
    path('login', login, name="login"),
]
