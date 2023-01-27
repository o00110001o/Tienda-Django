from django.urls import path 
from api_app.views import lista_plantas, detalle_planta
from api_app.viewsLogin import loginApi


urlpatterns = [
    path('lista_plantas', lista_plantas, name="lista_plantas"),
    path('detalle_planta/<id>', detalle_planta, name="detalle_planta"),
    path('loginApi', loginApi, name="loginApi"),

]
