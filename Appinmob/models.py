from django.db import models


# Create your models here.

class Inquilinos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
            return f"{self.id}- {self.nombre} {self.apellido} - {self.correo} - {self.telefono}" 
class Propietarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    telefono = models.IntegerField()
    CodigoDePropiedad = models.IntegerField()

    def __str__(self):
            return f" La propiedad numero:  {self.CodigoDePropiedad} corresponde a {self.nombre} {self.apellido}" 
    
class Empleados(models.Model): 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    empleadoId = models.IntegerField()

    def __str__(self):
        return f"{self.id}- {self.nombre} {self.apellido} - {self.empleadoId}"