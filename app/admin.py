from collections import UserList
from re import search
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Planta)
admin.site.register(Usuario)

