from django import forms
from django.core.validators import FileExtensionValidator
class InquilinoForm(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.IntegerField()


class PropietarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    correo = forms.EmailField()
    CodigoDePropiedad = forms.IntegerField()



class EmpleadoForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    empleadoId = forms.IntegerField()

class PropiedadForm(forms.Form):
    inmueble =forms.CharField(max_length=100, label= "Indique tipo de operacion ")
    ambientes=forms.IntegerField( label= "Indique cantidad de ambientes")
    contrato =forms.CharField(widget=forms.Textarea, label= "indique descripcion")
    ubicacion =forms.CharField(max_length=100, label="Inserte ubicacion")
    propietario =forms.CharField(max_length=100, label= 'indique propietario correspondiente')
    m2= forms.IntegerField( label= "Indique cantidad metros cuadrados")
    estado  =forms.CharField(max_length=100, label="Inserte estado de la propiedad")
    empleadoencargado= forms.CharField(max_length=100)
    fecha=  forms.DateTimeField()
    imagen = forms.FileField(required=False, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])], label="Imagen")

