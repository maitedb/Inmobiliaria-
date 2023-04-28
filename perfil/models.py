from django.db import models

# Create your models here.
class Empleados(models.Model): 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    empleadoId = models.IntegerField()
