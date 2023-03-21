from django.db import models

# Create your models here.

class inquilinos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    telefono = models.IntegerField()

class propietarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    telefono = models.IntegerField()
    CodigoDePropiedad = models.IntegerField()

class empleados(models.Model): 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    empleadoId = models.IntegerField()
