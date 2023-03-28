from django import forms 

class Guardar_inquilinoForm(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.IntegerField()


class Guardar_propietarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    CodigoDePropiedad = forms.IntegerField()

class Guardar_empleadoForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    empleadoId = forms.IntegerField()

class Buscar_PropietarioForm(forms.Form):
    CodigoDePropiedad = forms.IntegerField()


