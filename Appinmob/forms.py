from django import forms 

class InquilinoForm(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.IntegerField()


class PropietarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    CodigoDePropiedad = forms.IntegerField()

class EmpleadoForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    empleadoId = forms.IntegerField()

class PropietarioForm(forms.Form):
    CodigoDePropiedad = forms.IntegerField()


