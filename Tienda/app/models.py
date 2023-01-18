from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria =  models.IntegerField(primary_key = True, verbose_name = "Id de categoria")
    nombreCategoria = models.CharField(max_length = 50, verbose_name = "Nombre de la categoria")
    
    def _str_ (self):
        return self.nombreCategoria

class Plantas(models.Model):
    patente = models.CharField(max_length = 6, primary_key = True, verbose_name="Patente")
    marca = models.CharField(max_length = 20, verbose_name="Marca Vehiculo")
    modelo = models.CharField(max_length = 20, null = True, blank = True, verbose_name="Modelo")
    idCategoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
        
    def _str_ (self):
        return self.patente