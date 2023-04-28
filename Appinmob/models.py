from django.db import models


# Create your models here.

class Inquilinos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    telefono = models.IntegerField()

class Propietarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    telefono = models.IntegerField()
    CodigoDePropiedad = models.IntegerField()

class Propiedades(models.Model):
    inmuebble = models.CharField(max_length=100)
    ambientes= models.IntegerField()
    contrato= models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=140, default="")
    propietario = models.CharField(max_length=100)
    m2= models.IntegerField()
    estado= models.TextField(default="")
    imagen = models.ImageField(upload_to="media/propiedades", null=True, blank = True, default=None)
    empleadoencargado = models.CharField(max_length=100, default="")
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
