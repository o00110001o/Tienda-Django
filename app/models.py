from django.db import models
from datetime import datetime
from statistics import mode
from unittest.mock import create_autospec

# Create your models here.

class Categoria(models.Model):
    idCategoria =  models.IntegerField(primary_key = True, verbose_name = "Id de categoria")
    nombreCategoria = models.CharField(max_length = 50, verbose_name = "Nombre de la categoria")
    
    def __str__ (self):
        return self.nombreCategoria

class Planta(models.Model):
    codigo = models.CharField(max_length = 6, primary_key = True, verbose_name="Codigo")
    nombrePlanta = models.CharField(max_length = 20, verbose_name="Nombre Planta")
    precio = models.CharField(max_length = 20, null = True, blank = True, verbose_name="Precio") 
    idCategoria = models.ForeignKey('Categoria', verbose_name = "Nombre de la categoria", on_delete = models.CASCADE)
    
    def __str__ (self):
        return self.nombrePlanta
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField (max_length=20)
    correo = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tipo
    